# 📋 TigerGate Custom Rule Catalog

This catalog contains **21 custom SAST rules** (12 Python + 9 JavaScript) with matching vulnerable test files to verify each rule fires correctly.

---

## 🚀 How to Import Rules into TigerGate

1. Go to **TigerGate → Settings → Custom Rules → New Custom Rule**
2. Set **Name**, **Primary language**, and **Display severity** from the table below
3. Paste the **Rule body** (the `id:` → `metadata:` block) into the YAML editor
4. Click **Validate & Save**
5. Push this repo → rules should fire on the matching `vuln_*` files

---

## 🐍 Python Rules (12 rules)

**Rule file:** [`custom-rules/python-rules.yml`](custom-rules/python-rules.yml)

| # | Rule ID | Name | CWE | Severity | Trigger File |
|---|---------|------|-----|----------|--------------|
| 1 | `tg-py-eval-user-input` | Block dangerous eval() calls | CWE-95 | 🔴 Critical | `vuln_eval.py` |
| 2 | `tg-py-exec-user-input` | Block dangerous exec() calls | CWE-95 | 🔴 Critical | `vuln_eval.py` |
| 3 | `tg-py-os-system-injection` | OS command injection via os.system | CWE-78 | 🔴 Critical | `vuln_cmd.py` |
| 4 | `tg-py-subprocess-shell-true` | Subprocess with shell=True | CWE-78 | 🔴 Critical | `vuln_cmd.py` |
| 5 | `tg-py-weak-hash-md5` | MD5 weak hashing | CWE-327 | 🟡 Medium | `vuln_crypto.py` |
| 6 | `tg-py-weak-hash-sha1` | SHA1 weak hashing | CWE-327 | 🟡 Medium | `vuln_crypto.py` |
| 7 | `tg-py-hardcoded-password` | Hardcoded passwords | CWE-798 | 🟠 High | `vuln_secrets.py` |
| 8 | `tg-py-hardcoded-api-key` | Hardcoded API keys | CWE-798 | 🟠 High | `vuln_secrets.py` |
| 9 | `tg-py-pickle-load` | Unsafe pickle deserialization | CWE-502 | 🔴 Critical | `vuln_deserialize.py` |
| 10 | `tg-py-yaml-unsafe-load` | yaml.load without SafeLoader | CWE-502 | 🔴 Critical | `vuln_deserialize.py` |
| 11 | `tg-py-flask-debug-mode` | Flask debug mode enabled | CWE-215 | 🟠 High | `vuln_flask.py` |
| 12 | `tg-py-sql-injection-format` | SQL injection via string formatting | CWE-89 | 🔴 Critical | `vuln_flask.py` |
| — | `tg-py-ssrf-requests` | SSRF via requests.get/post | CWE-918 | 🟠 High | `vuln_flask.py` |
| — | `tg-py-path-traversal-open` | Path traversal via open() | CWE-22 | 🟠 High | `vuln_path.py` |

---

## 🟨 JavaScript / Node.js Rules (9 rules)

**Rule file:** [`custom-rules/javascript-rules.yml`](custom-rules/javascript-rules.yml)

| # | Rule ID | Name | CWE | Severity | Trigger File |
|---|---------|------|-----|----------|--------------|
| 1 | `tg-js-sql-injection-concat` | SQL injection via concatenation | CWE-89 | 🔴 Critical | `vuln_path.js`, `app.js` |
| 2 | `tg-js-xss-res-send` | Reflected XSS via res.send | CWE-79 | 🟠 High | `vuln_xss.js`, `app.js` |
| 3 | `tg-js-eval-injection` | eval() with dynamic input | CWE-95 | 🔴 Critical | `vuln_eval.js` |
| 4 | `tg-js-child-process-exec` | Command injection via exec() | CWE-78 | 🔴 Critical | `vuln_cmd.js` |
| 5 | `tg-js-hardcoded-jwt-secret` | Hardcoded JWT secret | CWE-798 | 🔴 Critical | `vuln_secrets.js` |
| 6 | `tg-js-nosql-injection` | NoSQL injection (MongoDB) | CWE-943 | 🟠 High | `vuln_nosql.js` |
| 7 | `tg-js-insecure-cookie` | Insecure cookie flags | CWE-614 | 🟡 Medium | `vuln_secrets.js` |
| 8 | `tg-js-path-traversal` | Path traversal via path.join | CWE-22 | 🟠 High | `vuln_path.js` |
| 9 | `tg-js-prototype-pollution` | Prototype pollution | CWE-1321 | 🟠 High | `vuln_prototype.js` |

---

## 📁 File Structure

```
sast_test_project/
├── custom-rules/
│   ├── python-rules.yml          ← 12 Python rules (copy into TigerGate UI)
│   └── javascript-rules.yml      ← 9 JavaScript rules
│
├── vuln_eval.py                  ← eval() / exec() injection
├── vuln_cmd.py                   ← os.system / subprocess injection
├── vuln_crypto.py                ← MD5 / SHA1 weak hashing
├── vuln_secrets.py               ← Hardcoded passwords & API keys
├── vuln_deserialize.py           ← pickle / yaml unsafe loading
├── vuln_flask.py                 ← SQLi + SSRF + debug mode
├── vuln_path.py                  ← Path traversal via open()
│
├── vuln_eval.js                  ← eval() injection
├── vuln_cmd.js                   ← child_process.exec injection
├── vuln_xss.js                   ← Reflected XSS via res.send
├── vuln_secrets.js               ← Hardcoded JWT + insecure cookies
├── vuln_nosql.js                 ← MongoDB NoSQL injection
├── vuln_path.js                  ← path.join traversal + SQLi
├── vuln_prototype.js             ← Prototype pollution
│
├── app.js                        ← Original SQLi + XSS (existing)
├── command.py                    ← Original cmd injection (existing)
├── config.py                     ← Original hardcoded secrets (existing)
└── Dockerfile                    ← Vulnerable container config (existing)
```

---

## 🧪 Testing Checklist

After importing all rules into TigerGate:

- [ ] Push the repo to trigger the SAST workflow
- [ ] Verify each rule fires with correct **file + line number**
- [ ] Confirm **severity** matches the rule definition
- [ ] Check **CWE mapping** is correct in the findings
- [ ] Validate no **false negatives** (every `❌ RULE HIT` comment should match a finding)

---

## ⚠️ Important Notes

- All code in `vuln_*` files is **intentionally vulnerable** — DO NOT use in production
- Rules use **Semgrep-style pattern syntax** (compatible with TigerGate's rule engine)
- `$USER_INPUT`, `$CMD`, `$DATA` etc. are **metavariables** that match any expression
- `...` in patterns means "zero or more arguments"
