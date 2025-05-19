import requests
import sys

def fingerprint(domain):
    try:
        r = requests.get(f"http://{domain}", timeout=10)
        headers = r.headers
        techs = []
        if "x-powered-by" in headers:
            techs.append(headers["x-powered-by"])
        if "server" in headers:
            techs.append("Server: " + headers["server"])
        if "set-cookie" in headers:
            if "PHPSESSID" in headers["set-cookie"]:
                techs.append("PHP")
            if "JSESSIONID" in headers["set-cookie"]:
                techs.append("Java")
        return techs
    except Exception as e:
        print(f"[-] Error: {e}")
        return []

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 techfinger.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"[~] Fingerprinting {domain}\n")
    techs = fingerprint(domain)
    if techs:
        for tech in techs:
            print(f"[+] {tech}")
    else:
        print("[-] No tech stack identified")
