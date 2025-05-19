import sys
import os

def extract_urls_with_params(input_file):
    urls_with_params = set()
    try:
        with open(input_file, 'r') as f:
            for line in f:
                line = line.strip()
                if '=' in line and '?' in line:
                    urls_with_params.add(line)
        return urls_with_params
    except Exception as e:
        print(f"[-] Error reading file: {e}")
        return set()

def save_output(output_file, urls):
    with open(output_file, 'w') as f:
        for url in sorted(urls):
            f.write(url + '\n')
    print(f"[+] Saved to {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 paramhunt.py <url_list_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    domain = os.path.basename(input_file).split('_')[0]
    output_file = f"output/{domain}_params.txt"

    print(f"[~] Extracting parameterized URLs from {input_file}\n")
    param_urls = extract_urls_with_params(input_file)
    print(f"[+] Found {len(param_urls)} URLs with parameters")
    save_output(output_file, param_urls)
