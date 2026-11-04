# Web Application Input Testing (Sanitized Lab 4 Portfolio)

This folder documents a controlled university cybersecurity lab involving HTTP input validation, XSS, CSRF, and Python-based automated vulnerability probing.

## What I implemented in the original lab
- Used Python `urllib.request` and `urllib.parse` to construct HTTP requests and inspect server responses.
- Tested up to 1,000 three-digit prefixes (000–999) to identify a deliberately introduced input-sanitization bypass.
- Compared reflected content to escaped output to detect potentially unsafe handling of user input.
- Used SSH port forwarding through a VPN to reach an isolated teaching environment.
- Validated the lab outcome through the course autograder.

This is systematic input enumeration and **fuzzing-related vulnerability testing**, not a claim of experience with AFL++, libFuzzer, Burp Suite, or production penetration testing.

## Safe reproduction
`input_validation_demo.py` is a **new, local-only demonstration** of the testing pattern. It never sends requests to the university lab or any external service, and it contains no credential collection or exploit payloads.

Run: `python3 input_validation_demo.py`

## Security and attribution
The original lab application, internal addresses, authentication material, cookies, and attack code are intentionally excluded. This is an independently written portfolio demonstration based on the concepts practiced in CSE 3140, not a copy of course starter code.
