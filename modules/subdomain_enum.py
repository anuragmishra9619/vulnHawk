import requests

def subdomain_scan(domain):
    subdomains = ['www', 'mail', 'blog', 'dev', 'test']
    found_subdomains = []

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 400:
                found_subdomains.append(url)
        except requests.ConnectionError:
            pass

    return found_subdomains
