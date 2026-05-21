/**
 * Trigger rules:
 *   - tg-js-nosql-injection  (MongoDB query with unsanitized input)
 * CWE-943: NoSQL Injection
 */
const express = require('express');
const app = express();
app.use(express.json());

// Simulated MongoDB collection
const db = {
  collection: (name) => ({
    find: (query) => ({ toArray: () => Promise.resolve([query]) }),
    findOne: (query) => Promise.resolve(query)
  })
};

const users = db.collection('users');
const orders = db.collection('orders');

// ── 🔴 NoSQL injection via find() ─────────────────────────────────────────
app.post('/api/login', async (req, res) => {
  // Attacker sends: { "username": {"$ne": ""}, "password": {"$ne": ""} }
  const user = await users.findOne({
    username: req.body.username, // ❌ RULE HIT: tg-js-nosql-injection
    password: req.body.password  // ❌ RULE HIT
  });
  if (user) {
    res.json({ message: "Logged in", user });
  } else {
    res.status(401).json({ message: "Invalid credentials" });
  }
});

// ── 🔴 NoSQL injection via find() with operator ───────────────────────────
app.post('/api/search', async (req, res) => {
  // Attacker sends: { "role": {"$gt": ""} }
  const results = await users.find({
    role: req.body.role // ❌ RULE HIT: tg-js-nosql-injection
  }).toArray();
  res.json(results);
});

module.exports = app;
