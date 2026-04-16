# Web Security Header Analyzer

## Overview  
A simple Python script that retrieves and displays HTTP response headers from a user-provided URL.  
This tool helps in analyzing server configurations and identifying important security-related headers.

---

## Features  
- 🔎 Fetches HTTP response headers from any website  
- 🔐 Highlights security-related headers  
- 🍪 Displays cookie attributes (HttpOnly, Secure, SameSite)  
- ⚡ Lightweight and easy to use (no external dependencies)  

---

## Tech Stack  
- Python 3  
- Built-in library: `urllib`  

---

## Installation  

```bash
git clone https://github.com/your-username/web-security-header-tool.git
cd web-security-header-tool
chmod +x Security-header-checker.py
python3 Security-header-checker.py


Usage
python Respones.py

Then enter the target URL:

Enter the URL (with https:// or http://): https://example.com

Sample Output
Response Headers
--------------------
Content-Type: text/html
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: default-src 'self'
Set-Cookie: sessionId=abc123; Secure; HttpOnly
Cache-Control: private
Security Insights

This tool helps in identifying:
- Missing or misconfigured security headers

Use Cases
Web Application Security Testing (VAPT)
Bug Bounty Recon
Learning HTTP Headers
Debugging API/Web responses

Disclaimer
This tool is intended for educational and authorized security testing purposes only.
Do not use it on systems without proper permission.

Author
Awdhesh Gupta
