"""
Trigger rules:
  - tg-py-flask-debug-mode     (Flask debug=True)
  - tg-py-sql-injection-format (SQL via f-string / format)
  - tg-py-ssrf-requests        (requests.get with user URL)
CWE-215, CWE-89, CWE-918
"""
from flask import Flask, request, redirect
import sqlite3
import requests

app = Flask(__name__)

# ── 🔴 SQL Injection via f-string ──────────────────────────────────────────
@app.route("/user")
def get_user():
    username = request.args.get("name")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{username}'")  # ❌ RULE HIT: tg-py-sql-injection-format
    return str(cursor.fetchall())

# ── 🔴 SQL Injection via .format() ─────────────────────────────────────────
@app.route("/order")
def get_order():
    order_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = {}".format(order_id))  # ❌ RULE HIT
    return str(cursor.fetchall())

# ── 🔴 SQL Injection via concatenation ─────────────────────────────────────
@app.route("/product")
def get_product():
    product_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = " + product_id + ";")  # ❌ RULE HIT
    return str(cursor.fetchall())

# ── 🔴 SQL Injection via % formatting ──────────────────────────────────────
@app.route("/search")
def search():
    keyword = request.args.get("q")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE '%%%s%%'" % keyword)  # ❌ RULE HIT
    return str(cursor.fetchall())

# ── 🔴 SSRF — requests.get with user-controlled URL ────────────────────────
@app.route("/fetch")
def fetch_url():
    target = request.args.get("url")
    resp = requests.get(target)  # ❌ RULE HIT: tg-py-ssrf-requests
    return resp.text

# ── 🔴 SSRF — requests.post with user-controlled URL ───────────────────────
@app.route("/webhook")
def webhook():
    callback_url = request.args.get("callback")
    resp = requests.post(callback_url, json={"status": "done"})  # ❌ RULE HIT
    return resp.text

# ── 🔴 Flask debug mode in production ──────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # ❌ RULE HIT: tg-py-flask-debug-mode
