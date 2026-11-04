"""Local-only, sanitized example of systematic input validation testing.

New portfolio demonstration; not the original CSE 3140 submission.
No network access or exploitation.
"""

def render_field(prefix: str, user_text: str) -> str:
    """Toy input handler with an intentionally introduced validation defect."""
    if prefix == "527":
        return user_text  # deliberately unsafe toy behavior
    return user_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def scan_inputs():
    marker = "<TEST_MARKER>"
    attempts = 0
    findings = []
    for number in range(1000):
        prefix = f"{number:03d}"
        attempts += 1
        output = render_field(prefix, marker)
        if marker in output:
            findings.append(prefix)
    return attempts, findings


if __name__ == "__main__":
    count, matches = scan_inputs()
    print(f"Inputs evaluated: {count}")
    print(f"Prefixes with unsafe reflection: {matches}")
    assert count == 1000
    assert matches == ["527"]
