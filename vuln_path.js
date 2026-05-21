/**
 * Trigger rules:
 *   - tg-js-path-traversal  (path.join with user input)
 *   - tg-js-sql-injection-concat (SQL via concatenation/template)
 * CWE-22: Path Traversal, CWE-89: SQL Injection
 */
const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

// Simulated DB
const db = { query: (q) => console.log("SQL:", q) };

// ── 🔴 Path traversal via path.join + req.query ───────────────────────────
app.get('/files', (req, res) => {
  const filePath = path.join('/var/uploads', req.query.filename); // ❌ RULE HIT: tg-js-path-traversal
  // Attacker: ?filename=../../../etc/passwd
  res.sendFile(filePath);
});

// ── 🔴 Path traversal via path.join + req.params ──────────────────────────
app.get('/docs/:docId', (req, res) => {
  const docPath = path.join('/app/documents', req.params.docId); // ❌ RULE HIT
  const content = fs.readFileSync(docPath, 'utf-8');
  res.send(content);
});

// ── 🔴 SQL Injection via template literal ─────────────────────────────────
app.get('/user/:id', (req, res) => {
  const userId = req.params.id;
  db.query(`SELECT * FROM users WHERE id = ${userId}`); // ❌ RULE HIT: tg-js-sql-injection-concat
  res.send("OK");
});

// ── 🔴 SQL Injection via string concatenation ────────────────────────────
app.get('/products', (req, res) => {
  const category = req.query.cat;
  db.query("SELECT * FROM products WHERE category = '" + category + "'"); // ❌ RULE HIT
  res.send("OK");
});

module.exports = app;
