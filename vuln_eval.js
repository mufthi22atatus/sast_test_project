/**
 * Trigger rules:
 *   - tg-js-eval-injection  (eval with dynamic input)
 * CWE-95: Code Injection
 */
const express = require('express');
const app = express();

// ── 🔴 eval() with query parameter ────────────────────────────────────────
app.get('/calc', (req, res) => {
  const expr = req.query.expression;
  const result = eval(expr); // ❌ RULE HIT: tg-js-eval-injection
  res.json({ result });
});

// ── 🔴 eval() with request body ───────────────────────────────────────────
app.post('/execute', (req, res) => {
  const code = req.body.code;
  const output = eval(code); // ❌ RULE HIT: tg-js-eval-injection
  res.json({ output });
});

module.exports = app;
