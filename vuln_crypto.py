"""
Trigger rules:
  - tg-py-weak-hash-md5   (MD5 usage)
  - tg-py-weak-hash-sha1  (SHA1 usage)
CWE-327: Use of a Broken or Risky Cryptographic Algorithm
"""
import hashlib

# ── 🔴 MD5 for password hashing ────────────────────────────────────────────
password = "supersecret123"
hashed_pw = hashlib.md5(password.encode()).hexdigest()  # ❌ RULE HIT: tg-py-weak-hash-md5
print(f"MD5 hash: {hashed_pw}")

# ── 🔴 MD5 for token generation ────────────────────────────────────────────
import time
token_data = f"user:admin:time:{time.time()}"
session_token = hashlib.md5(token_data.encode()).hexdigest()  # ❌ RULE HIT

# ── 🔴 SHA1 for integrity checking ─────────────────────────────────────────
file_content = b"important document contents"
checksum = hashlib.sha1(file_content).hexdigest()  # ❌ RULE HIT: tg-py-weak-hash-sha1
print(f"SHA1 checksum: {checksum}")

# ── 🔴 SHA1 for password verification ──────────────────────────────────────
def verify_password(pwd, stored_hash):
    return hashlib.sha1(pwd.encode()).hexdigest() == stored_hash  # ❌ RULE HIT
