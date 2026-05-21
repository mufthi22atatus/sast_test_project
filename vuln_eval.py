"""
Trigger rules:
  - tg-py-eval-user-input   (eval with user input)
  - tg-py-exec-user-input   (exec with user input)
CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code
"""

# ── 🔴 eval() with user input ──────────────────────────────────────────────
user_expr = input("Enter a math expression: ")
result = eval(user_expr)  # ❌ RULE HIT: tg-py-eval-user-input
print(f"Result: {result}")

# ── 🔴 eval() with request data (Flask-style) ──────────────────────────────
def compute(data):
    formula = data.get("formula", "1+1")
    return eval(formula)  # ❌ RULE HIT: tg-py-eval-user-input

# ── 🔴 exec() with user input ──────────────────────────────────────────────
code_snippet = input("Enter Python code to run: ")
exec(code_snippet)  # ❌ RULE HIT: tg-py-exec-user-input

# ── 🔴 exec() with external data ───────────────────────────────────────────
def run_plugin(plugin_code):
    exec(plugin_code)  # ❌ RULE HIT: tg-py-exec-user-input
