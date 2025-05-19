import re
import requests
import sys
import os
from urllib.parse import urljoin

def find_js_links(html, base_url):
    return re.findall(r'src=["\'](.*?\.js)["\']', html)

def fetch_js_files(urls):
    js_urls = set()
    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                found = find_js_links(r.text, url)
                for js in found:
                    full = urljoin(url, js)
                    js_urls.add(full)
        except Exception as e:
            continue
    return js_urls

def extract_secrets(js_url):
    try:
        r = requests.get(js_url, timeout=5)
        content = r.text
        findings = re.findall(r'(api_key|secret|token|apikey|access_token)["\']?\s*[:=]\s*["\'](.*?)["\']', content, re.I)
        return findings
    except:
        return []

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 jsleech.py <url_list_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    domain = os.path.basename(input_file).split('_')[0]
    with open(input_file) as f:
        urls = [x.strip() for x in f.readlines() if x.strip()]

    print(f"[~] Crawling {len(urls)} pages for JS files...")
    js_files = fetch_js_files(urls)
    print(f"[+] Found {len(js_files)} JS files\n")

    for js in js_files:
        secrets = extract_secrets(js)
        if secrets:
            print(f"[!] Potential secrets in {js}:")
            for s in secrets:
                print(f"    {s[0]}: {s[1]}")
