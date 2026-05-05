# 🛡️ SAST Test Project – Vulnerability Guide

This project is a **minimal intentionally vulnerable application** designed to test:
- SAST (Static Application Security Testing)
- Code Reviewers (PR-based scanning)
- Secret detection
- Container/image scanning

---

## 📁 Project Structure

```
app.js          → Node.js vulnerable endpoints
config.py       → Hardcoded secret
command.py      → Command injection example
Dockerfile      → Vulnerable container image
```

---

## 🚨 Vulnerabilities Included

### 1. SQL Injection (Critical)

**File:** `app.js`

```js
const query = "SELECT * FROM users WHERE id = " + id;
```

### 🔍 What is the issue?
User input (`id`) is directly concatenated into a SQL query without validation.

### ⚠️ Risk
Attackers can manipulate queries like:
```
?id=1 OR 1=1
```

### 💥 Impact
- Full database dump
- Authentication bypass
- Data modification/deletion

### 🛠 Fix
Use parameterized queries / prepared statements.

---

### 2. Cross-Site Scripting (XSS)

**File:** `app.js`

```js
res.send("<h1>" + req.query.q + "</h1>");
```

### 🔍 What is the issue?
User input is directly rendered in HTML.

### ⚠️ Risk
Attackers can inject scripts:
```
?q=<script>alert(1)</script>
```

### 💥 Impact
- Session hijacking
- Credential theft
- Malicious redirects

### 🛠 Fix
Escape output or use templating engines with auto-escaping.

---

### 3. Hardcoded Secret (High)

**File:** `config.py`

```python
API_KEY = "12345-SECRET-KEY"
```

### 🔍 What is the issue?
Sensitive credentials are stored in source code.

### ⚠️ Risk
Anyone with repo access can use this key.

### 💥 Impact
- Unauthorized API usage
- Account compromise

### 🛠 Fix
Use environment variables or secret managers.

---

### 4. Command Injection (Critical)

**File:** `command.py`

```python
os.system("cat " + user_input)
```

### 🔍 What is the issue?
User input is passed directly to system command.

### ⚠️ Risk
Attackers can execute arbitrary commands:
```
filename.txt; rm -rf /
```

### 💥 Impact
- Remote code execution
- System compromise

### 🛠 Fix
Use safe APIs like `subprocess.run()` with argument list.

---

### 5. Vulnerable Docker Image (Medium/High)

**File:** `Dockerfile`

```dockerfile
FROM node:12
```

### 🔍 What is the issue?
Outdated base image with known vulnerabilities.

### ⚠️ Risk
Includes OS/package CVEs.

### 💥 Impact
- Container compromise
- Supply chain risks

### 🛠 Fix
Use updated images like:
```
FROM node:18-alpine
```

---

## 🎯 Expected Findings in Code Reviewer

| Vulnerability        | Severity   | Detection Type |
|---------------------|-----------|---------------|
| SQL Injection       | Critical  | SAST          |
| XSS                 | High      | SAST          |
| Command Injection   | Critical  | SAST          |
| Hardcoded Secret    | High      | Secrets       |
| Vulnerable Image    | Medium    | SCA / Image   |

---

## 🧪 How to Test

1. Push this repo to your Git provider.
2. Enable your security scanning tool.
3. Run scan or create PR.
4. Verify:
   - Issues are detected
   - File + line numbers are correct
   - Severity is assigned properly

---

## ⚠️ Disclaimer

This project is intentionally insecure.  
Do NOT use in production.

---

## ✅ Goal

This repo helps you:
- Validate SAST pipeline
- Test real-time code review detection
- Demonstrate vulnerabilities quickly
