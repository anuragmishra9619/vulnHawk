import requests

def dir_bruteforce(target):
    common_dirs = ['admin', 'login', 'uploads', 'backup']
    found_dirs = []

    for d in common_dirs:
        url = f"http://{target}/{d}/"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                found_dirs.append(url)
        except requests.ConnectionError:
            pass

    return found_dirs
