# 🛡️ SAST Rule-Based Test Project (README)

This repository is a **minimal, rule-driven vulnerable project** designed to reliably trigger SAST (Static Application Security Testing) tools such as Atatus, Snyk, Semgrep, and GitHub Advanced Security.

---

# 🎯 Objective

The goal of this project is to:

- Trigger **guaranteed SAST detections**
- Validate **real-time code reviewer behavior**
- Map **code → rule → vulnerability (CWE)** clearly

---

# 📁 Project Files

```
app.js        → SQL Injection + XSS
command.py    → Command Injection + Path Traversal
config.py     → Hardcoded Secrets + Weak Crypto
Dockerfile    → Vulnerable container configuration
```

---

# 🚨 Vulnerabilities & Exact SAST Rules

---

## 1. SQL Injection (CWE-89)

**File:** `app.js`

```js
const userId = req.query.id;
const query = "SELECT * FROM users WHERE id = " + userId;
db.query(query);
```

### 🔍 Rule Pattern
- **Source:** `req.query.id`
- **Sink:** SQL query execution (`db.query`)
- **Condition:** String concatenation without sanitization

### 🧠 Rule Logic
```
IF user_input → string concatenation → SQL execution
THEN SQL Injection
```

---

## 2. Cross-Site Scripting (XSS) (CWE-79)

**File:** `app.js`

```js
const search = req.query.q;
res.send("<h1>" + search + "</h1>");
```

### 🔍 Rule Pattern
- **Source:** `req.query`
- **Sink:** HTML response (`res.send`)
- **Condition:** No escaping/encoding

### 🧠 Rule Logic
```
IF user_input → HTML response without encoding
THEN XSS
```

---

## 3. Command Injection (CWE-78)

**File:** `command.py`

```python
user_input = input()
os.system("cat " + user_input)
```

### 🔍 Rule Pattern
- **Source:** `input()`
- **Sink:** `os.system`
- **Condition:** Direct concatenation

### 🧠 Rule Logic
```
IF user_input → system command execution
THEN Command Injection
```

---

## 4. Path Traversal (CWE-22)

**File:** `command.py`

```python
file_name = input()
open("/tmp/" + file_name)
```

### 🔍 Rule Pattern
- **Source:** User input
- **Sink:** File path usage
- **Condition:** No validation

### 🧠 Rule Logic
```
IF user_input → file path construction
THEN Path Traversal
```

---

## 5. Hardcoded Secrets

**File:** `config.py`

```python
API_KEY = "sk_live_ABC123SECRET"
DB_PASSWORD = "rootpassword"
```

### 🔍 Rule Pattern
- Keywords: `API_KEY`, `PASSWORD`
- Value: Hardcoded string literal

### 🧠 Rule Logic
```
IF sensitive keyword → hardcoded value
THEN Secret Exposure
```

---

## 6. Weak Cryptography (CWE-327)

**File:** `config.py`

```python
hashlib.md5(password.encode())
```

### 🔍 Rule Pattern
- Use of weak algorithm: `MD5`

### 🧠 Rule Logic
```
IF MD5/SHA1 used for hashing
THEN Weak Crypto
```

---

## 7. Vulnerable Docker Configuration

**File:** `Dockerfile`

```dockerfile
FROM node:12
RUN apt-get install -y curl vim
COPY . .
```

### 🔍 Rule Patterns

#### a. Outdated Base Image
- `node:12` → known CVEs

#### b. Running as Root
- No USER specified

#### c. Broad Copy
- `COPY . .` → may expose secrets

### 🧠 Rule Logic
```
IF outdated base image → vulnerability
IF no USER specified → runs as root
IF COPY . . → potential secret exposure
```

---

# 📊 Expected SAST Findings

| Vulnerability        | CWE     | Severity  |
|---------------------|--------|----------|
| SQL Injection       | CWE-89 | Critical |
| XSS                 | CWE-79 | High     |
| Command Injection   | CWE-78 | Critical |
| Path Traversal      | CWE-22 | High     |
| Hardcoded Secrets   | -      | High     |
| Weak Crypto (MD5)   | CWE-327| Medium   |
| Docker Issues       | -      | Medium   |

---

# 🧪 Testing Instructions

1. Push this repo to your Git platform
2. Enable SAST scanning
3. Run scan or open PR
4. Verify:
   - Issues are detected
   - Correct severity assigned
   - File + line mapping works

---

# ⚠️ Notes

- This project is **intentionally insecure**
- Designed for **testing only**
- Do NOT deploy in production

---

# ✅ Key Insight

This repo is **rule-driven**, not random.

Each vulnerability exists specifically to match:
- Source → Sink pattern
- Known SAST rule signatures
- Industry-standard CWE mappings
