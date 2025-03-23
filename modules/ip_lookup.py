import requests

def ip_lookup(target):
    try:
        response = requests.get(f"https://ipinfo.io/{target}/json")
        return response.json()
    except:
        return {"error": "Failed to fetch IP info"}
