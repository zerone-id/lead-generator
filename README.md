# Lead Generator (Hono + Deno + Netlify Edge Functions)

A starter app scaffold using:

- [Hono](https://hono.dev/) for routing
- [Deno](https://deno.com/) as the runtime
- Netlify Edge Functions for deployment
- [Lucide](https://lucide.dev/) icons in the UI

## Project structure

- `netlify/edge-functions/app.ts` – Hono app entry for edge runtime
- `netlify.toml` – Netlify edge function routing config
- `deno.json` – Deno tasks and lint/fmt settings

## Local development

Prerequisites:

- Deno `>=1.40`
- Netlify CLI (`npm i -g netlify-cli`) for local edge emulation

Run locally with Netlify Edge:

```bash
netlify dev
```

Then open `http://localhost:8888`.

## Deno tasks

```bash
deno task check
deno task fmt
deno task lint
```

## Deploy

Push this repository and connect it to Netlify.

Netlify reads `netlify.toml` and serves the edge function at all paths.
