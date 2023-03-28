import requests
import sys
from termcolor import colored

if len(sys.argv) < 2:
    print("Created by: MrDzer0")
    print("===============================")
    print("Usage: python3 check.py <url>")
    
    sys.exit()

url = sys.argv[1]

response = requests.get(url)

# Check for X-XSS-Protection header
if "X-XSS-Protection" in response.headers:
    print(colored("X-XSS-Protection header found: " + response.headers["X-XSS-Protection"], 'green'))
else:
    print(colored("X-XSS-Protection header not found", 'red'))

# Check for X-Content-Type-Options header
if "X-Content-Type-Options" in response.headers:
    print(colored("X-Content-Type-Options header found: " + response.headers["X-Content-Type-Options"], 'green'))
else:
    print(colored("X-Content-Type-Options header not found", 'red'))

# Check for X-Frame-Options header
if "X-Frame-Options" in response.headers:
    print(colored("X-Frame-Options header found: " + response.headers["X-Frame-Options"], 'green'))
else:
    print(colored("X-Frame-Options header not found", 'red'))

# Check for Content-Security-Policy header
if "Content-Security-Policy" in response.headers:
    print(colored("Content-Security-Policy header found: " + response.headers["Content-Security-Policy"], 'green'))
else:
    print(colored("Content-Security-Policy header not found", 'red'))

# Check for Referrer-Policy header
if "Referrer-Policy" in response.headers:
    print(colored("Referrer-Policy header found: " + response.headers["Referrer-Policy"], 'green'))
else:
    print(colored("Referrer-Policy header not found", 'red'))

# Check for X-Permitted-Cross-Domain-Policies header
if "X-Permitted-Cross-Domain-Policies" in response.headers:
    print(colored("X-Permitted-Cross-Domain-Policies header found: " + response.headers["X-Permitted-Cross-Domain-Policies"], 'green'))
else:
    print(colored("X-Permitted-Cross-Domain-Policies header not found", 'red'))

# Check for X-Content-Duration header
if "X-Content-Duration" in response.headers:
    print(colored("X-Content-Duration header found: " + response.headers["X-Content-Duration"], 'green'))
else:
    print(colored("X-Content-Duration header not found", 'red'))

# Check for Strict-Transport-Security header
if "Strict-Transport-Security" in response.headers:
    print(colored("Strict-Transport-Security header found: " + response.headers["Strict-Transport-Security"], 'green'))
else:
    print(colored("Strict-Transport-Security header not found", 'red'))

# Check for Permissions-Policy header
if "Permissions-Policy" in response.headers:
    print(colored("Permissions-Policy header found: " + response.headers["Permissions-Policy"], 'green'))
else:
    print(colored("Permissions-Policy header not found", 'red'))

# Check for Server header
if "Server" in response.headers:
    print(colored("Server header found: " + response.headers["Server"], 'green'))
else:
    print(colored("Server header not found", 'red'))
