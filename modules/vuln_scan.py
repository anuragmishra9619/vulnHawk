import requests

def vuln_scan(target):
    vulnerabilities = []

    test_urls = [f"http://{target}/admin", f"http://{target}/phpmyadmin", f"http://{target}/backup"]
    for url in test_urls:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                vulnerabilities.append(url)
        except requests.ConnectionError:
            pass

    return vulnerabilities
