/**
 * Trigger rules:
 *   - tg-js-hardcoded-jwt-secret  (jwt.sign/verify with hardcoded secret)
 *   - tg-js-insecure-cookie       (cookie without httpOnly/secure)
 * CWE-798, CWE-614
 */
const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();

// ── 🔴 JWT signed with hardcoded secret ───────────────────────────────────
app.post('/login', (req, res) => {
  const user = { id: 1, role: 'admin' };
  const token = jwt.sign(user, "my-super-secret-jwt-key-123"); // ❌ RULE HIT: tg-js-hardcoded-jwt-secret
  res.json({ token });
});

// ── 🔴 JWT verified with hardcoded secret ─────────────────────────────────
app.get('/dashboard', (req, res) => {
  const token = req.headers.authorization;
  const decoded = jwt.verify(token, "my-super-secret-jwt-key-123"); // ❌ RULE HIT
  res.json({ user: decoded });
});

// ── 🔴 Cookie set without httpOnly/secure flags ───────────────────────────
app.get('/set-session', (req, res) => {
  res.cookie("sessionId", "abc123xyz"); // ❌ RULE HIT: tg-js-insecure-cookie
  res.send("Session set");
});

// ── 🔴 Cookie with httpOnly explicitly false ──────────────────────────────
app.get('/set-token', (req, res) => {
  res.cookie("authToken", "jwt-value-here", { httpOnly: false, secure: false }); // ❌ RULE HIT
  res.send("Token cookie set");
});

module.exports = app;
