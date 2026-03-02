import { Hono } from "npm:hono";

const app = new Hono();

app.get("/", (c) => {
  return c.html(`<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lead Generator</title>
    <style>
      :root {
        color-scheme: light dark;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
      }
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: radial-gradient(circle at top, #1f2937, #030712);
      }
      .card {
        width: min(680px, 92vw);
        border-radius: 16px;
        background: rgba(17, 24, 39, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.25);
        padding: 2rem;
        color: #e5e7eb;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
      }
      h1 {
        margin-top: 0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 1.75rem;
      }
      p {
        line-height: 1.7;
        color: #cbd5e1;
      }
      .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        border-radius: 999px;
        padding: 0.35rem 0.8rem;
        border: 1px solid rgba(125, 211, 252, 0.4);
        background: rgba(14, 116, 144, 0.28);
        color: #bae6fd;
        margin-top: 1rem;
        font-size: 0.9rem;
      }
    </style>
  </head>
  <body>
    <main class="card">
      <h1>
        <i data-lucide="rocket"></i>
        Hono + Deno on Netlify Edge
      </h1>
      <p>
        Your lead generator app scaffold is running successfully. This page is rendered by a
        <strong>Hono</strong> route in a <strong>Netlify Edge Function</strong> powered by
        <strong>Deno</strong>.
      </p>
      <span class="badge">
        <i data-lucide="sparkles"></i>
        Lucide icons enabled
      </span>
    </main>

    <script src="https://unpkg.com/lucide@latest"></script>
    <script>
      lucide.createIcons();
    </script>
  </body>
</html>`);
});

app.get("/health", (c) => c.json({ ok: true, runtime: "deno", framework: "hono" }));

export default (request: Request, context: unknown) => app.fetch(request, context);
