import requests
import sys
import json
from urllib.parse import urlparse

def get_crtsh(domain):
    print("[+] Querying crt.sh")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=10)
        data = json.loads(r.text)
        subdomains = set()
        for entry in data:
            name = entry['name_value']
            for sub in name.split('\n'):
                if domain in sub:
                    subdomains.add(sub.strip())
        return subdomains
    except Exception as e:
        print(f"[-] crt.sh failed: {e}")
        return set()

def get_bufferover(domain):
    print("[+] Querying dns.bufferover.run")
    try:
        url = f"https://dns.bufferover.run/dns?q=.\"{domain}\""
        r = requests.get(url, timeout=10)
        data = r.json()
        results = data.get("FDNS_A", [])
        subdomains = set()
        for item in results:
            sub = item.split(",")[1]
            if domain in sub:
                subdomains.add(sub.strip())
        return subdomains
    except Exception as e:
        print(f"[-] bufferover failed: {e}")
        return set()

def get_hackertarget(domain):
    print("[+] Querying HackerTarget")
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
        r = requests.get(url, timeout=10)
        lines = r.text.strip().split('\n')
        subdomains = set()
        for line in lines:
            sub = line.split(',')[0]
            if domain in sub:
                subdomains.add(sub.strip())
        return subdomains
    except Exception as e:
        print(f"[-] HackerTarget failed: {e}")
        return set()

def save_output(domain, subdomains):
    out_file = f"output/{domain}_subs.txt"
    with open(out_file, 'w') as f:
        for sub in sorted(subdomains):
            f.write(sub + '\n')
    print(f"[+] Saved to {out_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 subrecon.py <domain>")
        sys.exit(1)

    domain = sys.argv[1].strip()

    print(f"[~] Starting subdomain recon for {domain}\n")

    all_subdomains = set()
    all_subdomains.update(get_crtsh(domain))
    all_subdomains.update(get_bufferover(domain))
    all_subdomains.update(get_hackertarget(domain))

    print(f"\n[+] Total unique subdomains found: {len(all_subdomains)}")
    save_output(domain, all_subdomains)
