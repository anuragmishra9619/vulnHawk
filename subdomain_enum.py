import requests

# Subdomain Enumeration Function
def enumerate_subdomains(domain):
    subdomains = ["www", "mail", "ftp", "blog", "dev", "api", "test"]  # Sample subdomains
    found_subdomains = []

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                found_subdomains.append(url)
                print(f"[+] Found: {url}")
        except requests.exceptions.RequestException:
            pass  # Ignore errors

    return found_subdomains
