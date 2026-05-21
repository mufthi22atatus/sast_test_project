/**
 * Trigger rules:
 *   - tg-js-xss-res-send  (reflected XSS via res.send)
 * CWE-79: Cross-Site Scripting
 */
const express = require('express');
const app = express();

// ── 🔴 XSS via string concatenation ───────────────────────────────────────
app.get('/greet', (req, res) => {
  const name = req.query.name;
  res.send("<h1>Hello, " + name + "!</h1>"); // ❌ RULE HIT: tg-js-xss-res-send
});

// ── 🔴 XSS via template literal ───────────────────────────────────────────
app.get('/profile', (req, res) => {
  const user = req.query.user;
  res.send(`<div class="profile"><h2>${user}</h2></div>`); // ❌ RULE HIT: tg-js-xss-res-send
});

// ── 🔴 XSS with error message reflection ──────────────────────────────────
app.get('/error', (req, res) => {
  const msg = req.query.message;
  res.send("<div class='error'>" + msg + "</div>"); // ❌ RULE HIT
});

module.exports = app;
