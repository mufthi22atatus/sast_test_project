"""
Trigger rules:
  - tg-py-os-system-injection    (os.system with dynamic input)
  - tg-py-subprocess-shell-true  (subprocess with shell=True)
CWE-78: OS Command Injection
"""
import os
import subprocess

# ── 🔴 os.system() with string concatenation ───────────────────────────────
hostname = input("Enter hostname to ping: ")
os.system("ping -c 3 " + hostname)  # ❌ RULE HIT: tg-py-os-system-injection

# ── 🔴 os.system() with f-string ───────────────────────────────────────────
filename = input("Enter file to remove: ")
os.system(f"rm -rf /tmp/{filename}")  # ❌ RULE HIT: tg-py-os-system-injection

# ── 🔴 os.system() with .format() ──────────────────────────────────────────
ip_addr = input("Enter IP: ")
os.system("nslookup {}".format(ip_addr))  # ❌ RULE HIT: tg-py-os-system-injection

# ── 🔴 subprocess.call with shell=True ─────────────────────────────────────
user_cmd = input("Enter command: ")
subprocess.call(user_cmd, shell=True)  # ❌ RULE HIT: tg-py-subprocess-shell-true

# ── 🔴 subprocess.Popen with shell=True ────────────────────────────────────
log_path = input("Enter log file: ")
proc = subprocess.Popen(f"tail -f {log_path}", shell=True)  # ❌ RULE HIT

# ── 🔴 subprocess.run with shell=True ──────────────────────────────────────
domain = input("Enter domain: ")
subprocess.run(f"dig {domain}", shell=True, capture_output=True)  # ❌ RULE HIT
