const express = require('express');
const app = express();

// Simulated DB object (to make SAST tools recognize db.query sink)
const db = {
  query: (q) => {
    console.log("Executing query:", q);
  }
};

// 🔴 SQL Injection
app.get('/user', (req, res) => {
  const userId = req.query.id; // SOURCE
  const query = "SELECT * FROM users WHERE id = " + userId; // SINK ❌
  db.query(query);
  res.send("Query executed");
});

// 🔴 Reflected XSS
app.get('/search', (req, res) => {
  const search = req.query.q; // SOURCE
  res.send("<h1>Search: " + search + "</h1>"); // SINK ❌
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});