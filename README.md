# Bug Bounty Recon Tools
A collection of Python-based recon tools to aid in bug bounty hunting.

---

## Tools Included

### 1. `subrecon.py`
- Gathers subdomains via:
  - `crt.sh`
  - `dns.bufferover.run`
  - `hackertarget.com`
- Output: `output/<domain>_subs.txt`

### 2. `urlharvester.py`
- Collects archived URLs using the Wayback Machine
- Output: `output/<domain>_urls.txt`

### 3. `paramhunt.py`
- Filters URLs containing parameters
- Input: URL list file
- Output: `output/<domain>_params.txt`

### 4. `jsleech.py`
- Finds `.js` files from URL list
- Extracts potential secrets (API keys, tokens)

### 5. `dirprobe.py`
- Brute-forces common paths on target domain
- Requires wordlist input

### 6. `techfinger.py`
- Fingerprints server technology using HTTP headers

---

## 🚀 Usage
Make sure you have Python 3 installed.

...
pip install -r requirements.txt
```

Run each tool individually:

...
python3 subrecon.py example.com
python3 urlharvest.py example.com
python3 paramhunt.py output/example_urls.txt
python3 jsleech.py output/example_urls.txt
python3 dirprobe.py example.com wordlist.txt
python3 techfinger.py example.com
```

---

##Pro Tip
You can chain tools like this:

```bash
python3 subrecon.py target.com && \
python3 urlharvest.py target.com && \
python3 paramhunt.py output/target_urls.txt && \
python3 jsleech.py output/target_urls.txt
```

---

## Output Folder Structure
```
output/
  target_subs.txt
  target_urls.txt
  target_params.txt
```
