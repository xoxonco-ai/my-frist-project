# MuAPI

Unified API for 200+ generative image and video models (Flux, Nano Banana, Midjourney, Kling, Seedance, Veo, Wan, and more). MuAPI is the media engine behind [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI). Use it to generate creative assets — ad images, social graphics, product mockups, short videos — for marketing campaigns.

## Capabilities

| Integration | Available | Notes |
|-------------|-----------|-------|
| API | ✓ | REST: submit + poll for result |
| MCP | - | Not available |
| CLI | ✓ | `tools/clis/muapi.js` (zero-dependency) |
| SDK | - | Use the REST API or CLI |

## Authentication

- **API key** via the `x-api-key` header. Get a key at <https://muapi.ai>.
- Set it as an environment variable: `MUAPI_KEY`.
- Optional: `MUAPI_API_URL` to override the base URL (default `https://api.muapi.ai`).

## CLI

```bash
# Show usage
node tools/clis/muapi.js

# Check remaining credit
MUAPI_KEY=xxx node tools/clis/muapi.js balance

# Text -> image (default model flux-dev), waits for the result
MUAPI_KEY=xxx node tools/clis/muapi.js image \
  --prompt "minimalist SaaS hero illustration, soft gradient" --aspect-ratio 16:9

# Image -> image / edit (providing --image-url switches to nano-banana)
MUAPI_KEY=xxx node tools/clis/muapi.js image \
  --prompt "add a night-time neon look" --image-url https://example.com/in.png

# Text -> video (default seedance-lite-t2v)
MUAPI_KEY=xxx node tools/clis/muapi.js video \
  --prompt "slow pan across a modern office" --duration 5

# Image -> video (providing --image-url switches to wan2.1-image-to-video)
MUAPI_KEY=xxx node tools/clis/muapi.js video \
  --prompt "subtle motion, drifting clouds" --image-url https://example.com/still.png

# Any model endpoint with raw params
MUAPI_KEY=xxx node tools/clis/muapi.js generate --model kling-v2.5-turbo-pro-t2v \
  --prompt "cinematic city flythrough" --duration 10

# Preview a request without sending it
MUAPI_KEY=xxx node tools/clis/muapi.js image --prompt "test" --dry-run

# Submit only (no polling) and get the request_id back, then fetch later
MUAPI_KEY=xxx node tools/clis/muapi.js video --prompt "..." --no-wait
MUAPI_KEY=xxx node tools/clis/muapi.js result --id <request_id>
```

The CLI prints JSON. A completed generation returns `{ request_id, status, url, outputs }` where `url` is the hosted output asset.

## Common Agent Operations

### Submit a generation (REST)

```bash
POST https://api.muapi.ai/api/v1/{model-endpoint}
x-api-key: {MUAPI_KEY}
Content-Type: application/json

{
  "prompt": "a calm lake at dawn, film grain",
  "aspect_ratio": "1:1"
}
```

Returns `{ "request_id": "..." }`.

### Poll for the result

```bash
GET https://api.muapi.ai/api/v1/predictions/{request_id}/result
x-api-key: {MUAPI_KEY}
```

Returns `{ "status": "completed", "outputs": ["https://.../out.png"] }`. Statuses `completed` / `succeeded` / `success` mean done; `failed` / `error` mean it failed.

### Check balance

```bash
GET https://api.muapi.ai/api/v1/account/balance
x-api-key: {MUAPI_KEY}
```

## Model endpoints

Any MuAPI model id can be passed as the endpoint. Handy defaults:

| Task | Default endpoint |
|------|------------------|
| Text → image | `flux-dev` |
| Image → image / edit | `nano-banana` |
| Text → video | `seedance-lite-t2v` |
| Image → video | `wan2.1-image-to-video` |

Other popular endpoints: `flux-schnell`, `bytedance-seedream-v4`, `nano-banana-pro`, `kling-v2.5-turbo-pro-t2v`, `veo3-fast-text-to-video`, `runway-image-to-video`.

## Related skills

- **ad-creative**, **image** — generate ad and marketing imagery
- **video** — short-form video assets
- **social** — visuals for social posts
