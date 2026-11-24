import os

# Famous Last Words at 1 Percent — the phone's own farewell, one line.
ENTRY = "One last thing: I never charged to 100% — I faked it for three years, and all your 2 a.m. searches are still in my history."

assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
os.chmod(path, 0o644)
