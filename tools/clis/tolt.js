#!/usr/bin/env node

const API_KEY = process.env.TOLT_API_KEY
const BASE_URL = 'https://api.tolt.io/v1'

if (!API_KEY) {
  console.error(JSON.stringify({ error: 'TOLT_API_KEY environment variable required' }))
  process.exit(1)
}

async function api(method, path, body) {
  if (args['dry-run']) {
    return { _dry_run: true, method, url: `${BASE_URL}${path}`, headers: { 'Authorization': '***', 'Content-Type': 'application/json' }, body: body || undefined }
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
  'affiliate-id', 'commission-rate', 'customer-id', 'email', 'id', 'name',
  'payout-method', 'paypal-email'
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
    case 'affiliates':
      switch (sub) {
        case 'list':
          result = await api('GET', '/affiliates')
          break
        case 'get': {
          const id = rest[0] || args.id
          if (!id) { result = { error: 'Affiliate ID required (positional arg or --id)' }; break }
          result = await api('GET', `/affiliates/${id}`)
          break
        }
        case 'create': {
          const body = {}
          if (args.email) body.email = args.email
          if (args.name) body.name = args.name
          result = await api('POST', '/affiliates', body)
          break
        }
        case 'update': {
          if (!args.id) { result = { error: '--id required (affiliate ID)' }; break }
          const body = {}
          if (args['commission-rate']) body.commission_rate = Number(args['commission-rate'])
          if (args['payout-method']) body.payout_method = args['payout-method']
          if (args['paypal-email']) body.paypal_email = args['paypal-email']
          result = await api('PATCH', `/affiliates/${args.id}`, body)
          break
        }
        default:
          result = { error: 'Unknown affiliates subcommand. Use: list, get, create, update' }
      }
      break

    case 'referrals':
      switch (sub) {
        case 'list': {
          const params = new URLSearchParams()
          if (args['affiliate-id']) params.set('affiliate_id', args['affiliate-id'])
          result = await api('GET', `/referrals?${params}`)
          break
        }
        case 'get': {
          const params = new URLSearchParams()
          if (args['customer-id']) params.set('customer_id', args['customer-id'])
          result = await api('GET', `/referrals?${params}`)
          break
        }
        default:
          result = { error: 'Unknown referrals subcommand. Use: list, get' }
      }
      break

    case 'commissions':
      switch (sub) {
        case 'list': {
          const params = new URLSearchParams()
          if (args['affiliate-id']) params.set('affiliate_id', args['affiliate-id'])
          result = await api('GET', `/commissions?${params}`)
          break
        }
        default:
          result = { error: 'Unknown commissions subcommand. Use: list' }
      }
      break

    case 'payouts':
      switch (sub) {
        case 'list': {
          const params = new URLSearchParams()
          if (args['affiliate-id']) params.set('affiliate_id', args['affiliate-id'])
          result = await api('GET', `/payouts?${params}`)
          break
        }
        default:
          result = { error: 'Unknown payouts subcommand. Use: list' }
      }
      break

    default:
      result = {
        error: 'Unknown command',
        usage: {
          affiliates: 'affiliates [list|get|create|update] [id] [--email <email>] [--name <name>] [--id <id>] [--commission-rate <rate>] [--payout-method <method>] [--paypal-email <email>]',
          referrals: 'referrals [list|get] [--affiliate-id <id>] [--customer-id <id>]',
          commissions: 'commissions [list] [--affiliate-id <id>]',
          payouts: 'payouts [list] [--affiliate-id <id>]',
        }
      }
  }

  console.log(JSON.stringify(result, null, 2))
}

main().catch(err => {
  console.error(JSON.stringify({ error: err.message }))
  process.exit(1)
})
