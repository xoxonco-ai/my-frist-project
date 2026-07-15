#!/usr/bin/env node

// MuAPI CLI — generate images and videos through MuAPI (https://muapi.ai),
// the media engine behind Open Generative AI (200+ models: Flux, Nano Banana,
// Kling, Seedance, Veo…). Zero dependencies, Node 18+.
//
// Submits a generation request, polls until the output is ready, and prints
// the hosted output URL as JSON. Use --dry-run to preview the request without
// sending it, or --no-wait to submit and return the request_id immediately.

const API_KEY = process.env.MUAPI_KEY
const BASE_URL = (process.env.MUAPI_API_URL || 'https://api.muapi.ai').replace(/\/$/, '')
// Note: the MUAPI_KEY check is deferred to main() so `node muapi.js` (no args)
// can print usage without a key, per the repo's "no args = help" convention.

const DEFAULT_MODELS = {
  image: 'flux-dev',
  imageEdit: 'nano-banana',
  video: 'seedance-lite-t2v',
  imageToVideo: 'wan2.1-image-to-video',
}

// Known boolean flags never consume the following token as a value, so
// `--dry-run image` keeps `image` as a positional command instead of losing it.
const BOOLEAN_FLAGS = ['dry-run', 'no-wait']

function parseArgs(argv) {
  const result = { _: [] }
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i]
    if (arg.startsWith('--')) {
      const key = arg.slice(2)
      const next = argv[i + 1]
      if (next && !next.startsWith('--') && !BOOLEAN_FLAGS.includes(key)) {
        result[key] = next
        i++
      } else {
        result[key] = true
      }
    } else {
      result._.push(arg)
    }
  }
  return result
}

const args = parseArgs(process.argv.slice(2))

function headers() {
  return { 'Content-Type': 'application/json', 'x-api-key': API_KEY }
}

async function apiGet(path) {
  if (args['dry-run']) {
    return { _dry_run: true, method: 'GET', url: `${BASE_URL}${path}`, headers: { 'x-api-key': '***' } }
  }
  const res = await fetch(`${BASE_URL}${path}`, { headers: headers() })
  const text = await res.text()
  if (!res.ok) throw new Error(`${res.status} ${res.statusText} - ${text.slice(0, 200)}`)
  return text ? JSON.parse(text) : {}
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

async function pollForResult(requestId, maxAttempts, intervalMs) {
  const path = `/api/v1/predictions/${requestId}/result`
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    await sleep(intervalMs)
    try {
      const res = await fetch(`${BASE_URL}${path}`, { headers: headers() })
      if (!res.ok) {
        if (res.status >= 500) continue
        throw new Error(`Poll failed: ${res.status} - ${(await res.text()).slice(0, 200)}`)
      }
      const data = await res.json()
      const status = String(data.status || '').toLowerCase()
      if (status === 'completed' || status === 'succeeded' || status === 'success') return data
      if (status === 'failed' || status === 'error') throw new Error(`Generation failed: ${data.error || 'unknown error'}`)
    } catch (err) {
      // Tolerate transient network/JSON errors during the long poll; a video
      // job can run for many minutes and a brief blip shouldn't abort it.
      // But terminal failures — a failed generation, or a non-5xx "Poll failed"
      // (e.g. 401/404) — must propagate now, not retry up to maxAttempts.
      if (/Generation failed/.test(err.message) || /Poll failed/.test(err.message) || attempt === maxAttempts) throw err
    }
  }
  throw new Error('Generation timed out while polling for the result')
}

function outputUrl(data) {
  return (
    (Array.isArray(data.outputs) && data.outputs[0]) ||
    data.url ||
    (typeof data.output === 'string' ? data.output : data.output && data.output.url) ||
    null
  )
}

// Submit a generation, then (unless --no-wait) poll until complete.
async function submit(model, payload, maxAttempts) {
  if (args['dry-run']) {
    return { _dry_run: true, method: 'POST', url: `${BASE_URL}/api/v1/${model}`, headers: { 'x-api-key': '***' }, body: payload }
  }
  const res = await fetch(`${BASE_URL}/api/v1/${model}`, {
    method: 'POST',
    headers: headers(),
    body: JSON.stringify(payload),
  })
  const text = await res.text()
  if (!res.ok) throw new Error(`${res.status} ${res.statusText} - ${text.slice(0, 200)}`)
  const data = text ? JSON.parse(text) : {}
  const requestId = data.request_id || data.id
  if (!requestId) return data
  if (args['no-wait']) return { request_id: requestId, status: 'submitted' }
  try {
    const result = await pollForResult(requestId, maxAttempts, 2000)
    return { request_id: requestId, status: result.status, url: outputUrl(result), outputs: result.outputs || undefined }
  } catch (err) {
    // Surface the request_id so a long job can be recovered via `result --id`.
    err.message = `${err.message} (request_id: ${requestId}; retry with: muapi.js result --id ${requestId})`
    throw err
  }
}

const ACTIVE_COMMANDS = ['balance', 'image', 'video', 'generate', 'result']

async function main() {
  const [cmd] = args._
  let result

  // Only commands that hit the API need a key; usage/help works without one.
  if (ACTIVE_COMMANDS.includes(cmd) && !API_KEY) {
    console.error(JSON.stringify({ error: 'MUAPI_KEY environment variable required (get one at https://muapi.ai)' }))
    process.exit(1)
  }

  switch (cmd) {
    case 'balance':
      result = await apiGet('/api/v1/account/balance')
      break

    case 'image': {
      if (!args.prompt) { result = { error: 'image requires --prompt' }; break }
      const model = args.model || (args['image-url'] ? DEFAULT_MODELS.imageEdit : DEFAULT_MODELS.image)
      const payload = { prompt: args.prompt }
      if (args['aspect-ratio']) payload.aspect_ratio = args['aspect-ratio']
      if (args.resolution) payload.resolution = args.resolution
      if (args.quality) payload.quality = args.quality
      if (args['image-url']) payload.image_url = args['image-url']
      if (args.seed) payload.seed = Number(args.seed)
      result = await submit(model, payload, 120)
      break
    }

    case 'video': {
      const model = args.model || (args['image-url'] ? DEFAULT_MODELS.imageToVideo : DEFAULT_MODELS.video)
      const payload = {}
      if (args.prompt) payload.prompt = args.prompt
      if (args['aspect-ratio']) payload.aspect_ratio = args['aspect-ratio']
      if (args.resolution) payload.resolution = args.resolution
      if (args.quality) payload.quality = args.quality
      if (args.duration) payload.duration = Number(args.duration)
      if (args.mode) payload.mode = args.mode
      if (args['image-url']) payload.image_url = args['image-url']
      if (!payload.prompt && !payload.image_url) { result = { error: 'video requires --prompt or --image-url' }; break }
      result = await submit(model, payload, 900)
      break
    }

    case 'generate': {
      // Raw passthrough: --model <endpoint> plus common fields.
      if (!args.model) { result = { error: 'generate requires --model <endpoint>' }; break }
      const payload = {}
      if (args.prompt) payload.prompt = args.prompt
      if (args['aspect-ratio']) payload.aspect_ratio = args['aspect-ratio']
      if (args.resolution) payload.resolution = args.resolution
      if (args.quality) payload.quality = args.quality
      if (args.duration) payload.duration = Number(args.duration)
      if (args['image-url']) payload.image_url = args['image-url']
      if (args.seed) payload.seed = Number(args.seed)
      result = await submit(args.model, payload, 900)
      break
    }

    case 'result': {
      if (!args.id) { result = { error: 'result requires --id <request_id>' }; break }
      result = await apiGet(`/api/v1/predictions/${args.id}/result`)
      break
    }

    default:
      result = {
        error: 'Unknown command',
        usage: {
          balance: 'balance',
          image: 'image --prompt <text> [--model flux-dev] [--aspect-ratio 1:1] [--image-url <url>] [--seed <n>] [--no-wait]',
          video: 'video --prompt <text> [--model seedance-lite-t2v] [--image-url <url>] [--duration <s>] [--no-wait]',
          generate: 'generate --model <endpoint> [--prompt <text>] [--image-url <url>] [--duration <s>]',
          result: 'result --id <request_id>',
          options: '--dry-run (preview request)  --no-wait (submit only, return request_id)',
          env: 'MUAPI_KEY (required), MUAPI_API_URL (optional, default https://api.muapi.ai)',
        },
      }
  }

  console.log(JSON.stringify(result, null, 2))
}

main().catch((err) => {
  console.error(JSON.stringify({ error: err.message }))
  process.exit(1)
})
