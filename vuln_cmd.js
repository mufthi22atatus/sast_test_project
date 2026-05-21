/**
 * Trigger rules:
 *   - tg-js-child-process-exec  (child_process.exec with user input)
 * CWE-78: OS Command Injection
 */
const express = require('express');
const { exec } = require('child_process');
const app = express();

// ── 🔴 exec() with string concatenation ───────────────────────────────────
app.get('/ping', (req, res) => {
  const host = req.query.host;
  exec("ping -c 3 " + host, (err, stdout) => { // ❌ RULE HIT: tg-js-child-process-exec
    res.send(stdout);
  });
});

// ── 🔴 exec() with template literal ───────────────────────────────────────
app.get('/dns', (req, res) => {
  const domain = req.query.domain;
  exec(`nslookup ${domain}`, (err, stdout) => { // ❌ RULE HIT: tg-js-child-process-exec
    res.send(stdout);
  });
});

// ── 🔴 exec() with file operations ────────────────────────────────────────
app.get('/logs', (req, res) => {
  const logfile = req.query.file;
  exec(`cat /var/log/${logfile}`, (err, stdout) => { // ❌ RULE HIT
    res.send(stdout);
  });
});

module.exports = app;
