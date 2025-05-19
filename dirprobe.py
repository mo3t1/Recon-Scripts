import sys
import os
import requests

def load_wordlist(path):
    try:
        with open(path, 'r') as f:
            return [x.strip() for x in f if x.strip()]
    except:
        print("[-] Wordlist not found.")
        return []

def probe_paths(domain, wordlist):
    found = []
    for path in wordlist:
        url = f"http://{domain}/{path}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code < 400:
                print(f"[+] {url} => {r.status_code}")
                found.append(url)
        except:
            continue
    return found

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 dirprobe.py <domain> <wordlist>")
        sys.exit(1)

    domain = sys.argv[1].strip()
    wordlist_file = sys.argv[2].strip()

    paths = load_wordlist(wordlist_file)
    print(f"[~] Probing {len(paths)} paths...")
    results = probe_paths(domain, paths)
    print(f"\n[+] Found {len(results)} valid paths")
