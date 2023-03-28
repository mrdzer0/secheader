# Security Header Checker

This is a simple Python script that checks for security headers in a given URL and returns the result.

## Requirements

This script requires Python 3.x and the `requests` module to be installed.

## How to use
```
python3 secheader.py https://example.com
```

## Information

This will check for all the security headers as well as the `Strict-Transport-Security`, `Permissions-Policy`, and `Server` headers for the specified URL.

The script will return a table showing the status of each header. A green color means that the header is present, while a red color means that the header is not present.

## Security Headers Checked

The script checks for the following security headers:

- X-XSS-Protection
- X-Content-Type-Options
- Referrer-Policy
- Content-Security-Policy
- X-Frame-Options
- Strict-Transport-Security
- Permissions-Policy
- Server

## License

This script is released under the MIT License. See the [LICENSE](LICENSE) file for details.
