import json
from fp.fp import FreeProxy
import requests


def refreshProxies():
    with open("data/proxies.json", "w", encoding="utf-8") as f:
        json.dump([],f)


def findProxies(no=10, refreshFile=True):
    # Load existing proxies from file or start with empty 
    if refreshFile==True:
        refreshProxies()

    try:
        with open("data/proxies.json", "r", encoding="utf-8") as f:
            existing_proxies = set(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        existing_proxies = set()

    # Create a new set of proxies
    new_proxies = set()
    for _ in range(no):
        new_proxies.add(FreeProxy(elite=True).get())

    # Combine sets to remove duplicates
    all_proxies = existing_proxies.union(new_proxies)

    # Save the unique proxies back to the file
    with open("data/proxies.json", "w", encoding="utf-8") as f:
        json.dump(list(all_proxies), f, indent=4)


def getProxies():
    try:
        with open("data/proxies.json", "r", encoding="utf-8") as f:
            existing_proxies = set(json.load(f))
            return existing_proxies
    except (FileNotFoundError, json.JSONDecodeError):
        raise Exception("Proxy file is empty, try running findProxies()")
    

def request_with_proxies(url, proxy_list, timeout=10, debug=False):
    for proxy in proxy_list:
        print(f"[*] Trying proxy: {proxy}")
        try:
            response = requests.get(
                url,
                proxies={"http": proxy, "https": proxy},
                timeout=timeout
            )
            response.raise_for_status()
            print(f"[✓] Success with proxy: {proxy}")
            if debug:
                print(response.text)
            return response
        except Exception as e:
            print(f"[✗] Failed with proxy {proxy}: {e}")
    raise Exception("All proxies failed.")


if __name__ == "__main__":
    proxylist=getProxies()
    request_with_proxies("https://api.ipify.org?format=json",proxylist,10,True)