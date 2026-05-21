"""
Trigger rules:
  - tg-py-hardcoded-password   (hardcoded passwords)
  - tg-py-hardcoded-api-key    (hardcoded API keys)
CWE-798: Use of Hard-coded Credentials
"""

# ── 🔴 Hardcoded passwords ─────────────────────────────────────────────────
PASSWORD = "admin123!@#"  # ❌ RULE HIT: tg-py-hardcoded-password
password = "p@ssw0rd_2024"  # ❌ RULE HIT
DB_PASSWORD = "mysql_root_secret"  # ❌ RULE HIT

# ── 🔴 Hardcoded API keys ──────────────────────────────────────────────────
API_KEY = "dummy_stripe_sk_live_key_for_testing_12345"  # ❌ RULE HIT: tg-py-hardcoded-api-key
SECRET_KEY = "dummy_stripe_whsec_key_for_testing_12345"  # ❌ RULE HIT
AWS_SECRET_ACCESS_KEY = "dummy_aws_secret_access_key_for_testing_12345"  # ❌ RULE HIT

# ── Usage in code ───────────────────────────────────────────────────────────
import requests

def call_payment_api(amount):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    return requests.post("https://api.stripe.com/v1/charges",
                         headers=headers, data={"amount": amount})

def connect_db():
    import mysql.connector
    return mysql.connector.connect(
        host="db.prod.internal",
        user="root",
        password=DB_PASSWORD,  # Using the hardcoded credential
        database="production"
    )
