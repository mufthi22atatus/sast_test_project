"""
Trigger rule:
  - tg-py-path-traversal-open  (open() with user-controlled path)
CWE-22: Path Traversal
"""
from flask import Flask, request, send_file

app = Flask(__name__)

# ── 🔴 open() with concatenation ───────────────────────────────────────────
@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open("/var/data/" + filename, "r") as f:  # ❌ RULE HIT: tg-py-path-traversal-open
        return f.read()

# ── 🔴 open() with f-string ────────────────────────────────────────────────
@app.route("/download")
def download():
    doc = request.args.get("doc")
    with open(f"/uploads/{doc}", "rb") as f:  # ❌ RULE HIT: tg-py-path-traversal-open
        return f.read()

# ── 🔴 send_file with user path ────────────────────────────────────────────
@app.route("/serve")
def serve_file():
    filepath = request.args.get("path")
    return send_file("/static/" + filepath)  # Also a path traversal vector

if __name__ == "__main__":
    app.run(port=5001)
