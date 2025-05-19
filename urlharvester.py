mport requests
import sys
import os
from urllib.parse import urlparse

def fetch_waybackurls(domain):
    print("[+] Fetching from Wayback Machine")
    url = f"http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=text&fl=original&collapse=urlkey"
    try:
        r = requests.get(url, timeout=10)
        urls = set(r.text.strip().split('\n'))
        return urls
    except Exception as e:
        print(f"[-] Wayback failed: {e}")
        return set()

def save_output(domain, urls):
    if not os.path.exists("output"):
        os.makedirs("output")
    out_file = f"output/{domain}_urls.txt"
    with open(out_file, 'w') as f:
        for u in sorted(urls):
            f.write(u + '\n')
    print(f"[+] Saved to {out_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 urlharvest.py <domain>")
        sys.exit(1)

    domain = sys.argv[1].strip()
    print(f"[~] Harvesting URLs for {domain}\n")
    urls = fetch_waybackurls(domain)
    print(f"\n[+] Total URLs found: {len(urls)}")
    save_output(domain, urls)

