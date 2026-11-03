#!/usr/bin/env node

const API_KEY = process.env.DUB_API_KEY
const BASE_URL = 'https://api.dub.co'

if (!API_KEY) {
  console.error(JSON.stringify({ error: 'DUB_API_KEY environment variable required' }))
  process.exit(1)
}

async function api(method, path, body) {
  if (args['dry-run']) {
    return { _dry_run: true, method, url: `${BASE_URL}${path}`, headers: { Authorization: '***', 'Content-Type': 'application/json' }, body: body || undefined }
  }
  const res = await fetch(`${BASE_URL}${path}`, {
    method,
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: body ? JSON.stringify(body) : undefined,
  })
  const text = await res.text()
  if (!res.ok) process.exitCode = 1
  try {
    return JSON.parse(text)
  } catch {
    return { status: res.status, body: text }
  }
}

const { parseArgs } = require('node:util')

// Every --flag this CLI reads; node:util.parseArgs needs each one typed
// up front (strict: false still allows unlisted flags, just without
// value-capture).
const STRING_FLAGS = [
  'domain', 'external-id', 'id', 'interval', 'key', 'link-id', 'links',
  'page', 'tags', 'url'
]
const options = { 'dry-run': { type: 'boolean' } }
for (const flag of STRING_FLAGS) options[flag] = { type: 'string' }

const { values, positionals } = parseArgs({
  args: process.argv.slice(2),
  options,
  strict: false,
  allowPositionals: true,
})
const args = { ...values, _: positionals }
const [cmd, sub, ...rest] = args._

async function main() {
  let result

  switch (cmd) {
    case 'links':
      switch (sub) {
        case 'create': {
          if (!args.url) { result = { error: '--url required' }; break }
          const body = {}
          if (args.url) body.url = args.url
          if (args.domain) body.domain = args.domain
          if (args.key) body.key = args.key
          if (args.tags) body.tags = args.tags.split(',')
          result = await api('POST', '/links', body)
          break
        }
        case 'list': {
          const params = new URLSearchParams()
          if (args.domain) params.set('domain', args.domain)
          if (args.page) params.set('page', args.page)
          result = await api('GET', `/links?${params}`)
          break
        }
        case 'get': {
          const params = new URLSearchParams()
          if (args.domain) params.set('domain', args.domain)
          if (args.key) params.set('key', args.key)
          if (args['link-id']) params.set('linkId', args['link-id'])
          if (args['external-id']) params.set('externalId', args['external-id'])
          result = await api('GET', `/links/info?${params}`)
          break
        }
        case 'update': {
          if (!args.id) { result = { error: '--id required (link ID)' }; break }
          const body = {}
          if (args.url) body.url = args.url
          if (args.tags) body.tags = args.tags.split(',')
          result = await api('PATCH', `/links/${args.id}`, body)
          break
        }
        case 'delete':
          if (!args.id) { result = { error: '--id required (link ID)' }; break }
          result = await api('DELETE', `/links/${args.id}`)
          break
        case 'bulk-create': {
          let links
          try {
            links = JSON.parse(args.links || '[]')
          } catch {
            result = { error: 'Invalid JSON in --links' }; break
          }
          result = await api('POST', '/links/bulk', links)
          break
        }
        default:
          result = { error: 'Unknown links subcommand. Use: create, list, get, update, delete, bulk-create' }
      }
      break

    case 'analytics':
      switch (sub) {
        case 'get': {
          const params = new URLSearchParams()
          if (args.domain) params.set('domain', args.domain)
          if (args.key) params.set('key', args.key)
          if (args.interval) params.set('interval', args.interval)
          result = await api('GET', `/analytics?${params}`)
          break
        }
        case 'country': {
          const params = new URLSearchParams()
          if (args.domain) params.set('domain', args.domain)
          if (args.key) params.set('key', args.key)
          result = await api('GET', `/analytics/country?${params}`)
          break
        }
        case 'device': {
          const params = new URLSearchParams()
          if (args.domain) params.set('domain', args.domain)
          if (args.key) params.set('key', args.key)
          result = await api('GET', `/analytics/device?${params}`)
          break
        }
        default:
          result = { error: 'Unknown analytics subcommand. Use: get, country, device' }
      }
      break

    default:
      result = {
        error: 'Unknown command',
        usage: {
          links: 'links [create|list|get|update|delete|bulk-create] [--url <url>] [--domain <domain>] [--key <key>] [--tags <tags>] [--id <id>] [--page <page>] [--links <json>]',
          analytics: 'analytics [get|country|device] [--domain <domain>] [--key <key>] [--interval <interval>]',
        }
      }
  }

  console.log(JSON.stringify(result, null, 2))
}

main().catch(err => {
  console.error(JSON.stringify({ error: err.message }))
  process.exit(1)
})
