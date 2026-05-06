import hashlib

# 🔴 Hardcoded Secrets
API_KEY = "sk_live_ABC123SECRET"  # ❌
DB_PASSWORD = "rootpassword"      # ❌

# 🔴 Weak Cryptography
password = "admin123"
hashed = hashlib.md5(password.encode()).hexdigest()  # ❌ weak hashing

print("Hashed password:", hashed)