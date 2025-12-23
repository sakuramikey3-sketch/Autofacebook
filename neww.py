import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--- Colors ---
H = "\x1b[38;5;46m"  # Hara
M = "\x1b[38;5;196m" # Laal
P = "\x1b[38;5;231m" # Safaid
A = "\x1b[38;5;248m" # Abu

class PakProRotation:
    def __init__(self):
        self.ses = requests.Session()
        self.mail_api = "https://api.mail.tm"
        self.proxies = []
        self.ok = 0
        self.cp = 0
        self.main_menu()

    def logo(self):
        os.system('clear')
        print(f"{H}--- PAK FB PRO (PROXY ROTATION) ---{P}")
        print(f"{M}>> {P}Status: Undetectable | Proxy: Active")
        print(f"------------------------------------------")

    # --- Proxy Scraper (Har baar naya IP) ---
    def scrape_proxies(self):
        print(f" {A}└─ Fetching fresh proxies for Pakistan...", end='\r')
        try:
            res = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
            self.proxies = res.splitlines()
            print(f" {H}└─ Found {len(self.proxies)} Proxies!            ")
        except:
            print(f" {M}└─ Proxy Fetch Failed! Using Direct IP.    ")

    def get_proxy(self):
        if self.proxies:
            proxy = random.choice(self.proxies)
            return {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        return None

    # --- Mail.tm Verification ---
    def create_mail(self, proxy):
        try:
            domain_res = requests.get(f"{self.mail_api}/domains", proxies=proxy, timeout=10).json()
            domain = domain_res['hydra:member'][0]['domain']
            user = f"pak_pro_{random.getrandbits(16)}"
            password = "pass"+str(random.randint(111,999))
            data = {"address": f"{user}@{domain}", "password": password}
            res = requests.post(f"{self.mail_api}/accounts", json=data, proxies=proxy, timeout=10)
            if res.status_code == 201:
                token_res = requests.post(f"{self.mail_api}/token", json=data, proxies=proxy, timeout=10).json()
                return f"{user}@{domain}", token_res['token']
        except: return None, None

    def start(self):
        self.scrape_proxies()
        limit = int(input(f"{M}>>{P} Kitni IDs banani hain?: "))
        
        for _ in range(limit):
            current_proxy = self.get_proxy()
            name = f"Muhammad {random.choice(['Zain', 'Haris', 'Umar', 'Afridi'])}"
            email, token = self.create_mail(current_proxy)

            if not email:
                print(f"{M}[!] Proxy Error, Switching...")
                continue

            print(f"\n{H}[+] Creating ID with Proxy: {current_proxy['http']}")
            print(f" {A}└─ Name: {name} | Email: {email}")

            # Registration and Login Check Logic here...
            # (Pichle codes ki tarah)
            
            time.sleep(5)

    def main_menu(self):
        self.logo()
        print(f"[{H}1{P}] Start Pro-Creation (Proxy Mode)")
        if input(f"\n{M}>>{P} Select: ") == '1': self.start()

if __name__ == "__main__":
    PakProRotation()
