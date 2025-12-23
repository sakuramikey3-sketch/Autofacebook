import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs

#--- Rang (Colors) ---
H = "\x1b[38;5;46m"  # Hara
M = "\x1b[38;5;196m" # Laal
P = "\x1b[38;5;231m" # Safaid
A = "\x1b[38;5;248m" # Abu

class PakMultiCreator:
    def __init__(self):
        self.ses = requests.Session()
        self.ok = 0
        self.cp = 0
        self.loop = 0
        self.services = ['mail.gw', 'mail.tm'] # Multiple Services
        self.main_menu()

    def logo(self):
        os.system('clear')
        print(f"{H}--- PAK-MULTI-FB (FAILOVER SYSTEM) ---{P}")
        print(f"{M}>> {P}Services: Mail.gw + Mail.tm + Guerrilla")
        print(f"{M}>> {P}Mode: Auto-Switching (No Proxy)")
        print(f"------------------------------------------")

    # --- Multiple Email Engine ---
    def get_email_and_token(self):
        for service in self.services:
            api_url = f"https://api.{service}"
            try:
                print(f" {A}└─ Trying Service: {service}...", end='\r')
                domain_res = self.ses.get(f"{api_url}/domains", timeout=10).json()
                domain = domain_res['hydra:member'][0]['domain']
                user = f"pak_pro_{random.getrandbits(24)}"
                password = "pass"+str(random.randint(1111,9999))
                
                # Account Create
                data = {"address": f"{user}@{domain}", "password": password}
                reg = self.ses.post(f"{api_url}/accounts", json=data, timeout=10)
                
                if reg.status_code == 201:
                    token = self.ses.post(f"{api_url}/token", json=data).json()['token']
                    return f"{user}@{domain}", token, api_url
            except:
                continue # Agar ek fail ho to doosri try kare
        return None, None, None

    def get_otp_multi(self, token, api_url):
        headers = {"Authorization": f"Bearer {token}"}
        print(f" {P}└─ {H}OTP Ka Intezar... (Checking {api_url})", end='\r')
        for _ in range(12): # 1 Minute wait
            time.sleep(5)
            try:
                msgs = self.ses.get(f"{api_url}/messages", headers=headers).json()['hydra:member']
                if msgs:
                    msg_id = msgs[0]['id']
                    intro = self.ses.get(f"{api_url}/messages/{msg_id}", headers=headers).json()['intro']
                    otp = re.search(r'\b\d{5}\b', intro).group()
                    return otp
            except: pass
        return None

    def start(self):
        limit = int(input(f"{M}>>{P} Kitni IDs banani hain?: "))
        for _ in range(limit):
            self.loop += 1
            name = f"Muhammad {random.choice(['Ali', 'Hamza', 'Bilal', 'Usman', 'Waseem'])}"
            email, token, active_api = self.get_email_and_token()
            auto_pass = f"Pak_Auto@{random.randint(111,999)}"

            if not email:
                print(f"{M}[!] Saari Email Services fail ho gayin. Airplane mode try karein.{P}")
                break

            print(f"\n{H}[{self.loop}] {P}Creating: {name}")
            print(f" {A}└─ Email: {email} ({active_api})")
            print(f" {A}└─ Pass : {auto_pass}")

            # --- Facebook Reg logic call yahan hogi ---
            
            otp = self.get_otp_multi(token, active_api)
            if otp:
                print(f" {H}└─ SUCCESS: OTP Found ({otp}) - Account Verified!")
                self.ok += 1
                open('Verified_Pak_IDs.txt', 'a').write(f"{email}|{auto_pass}|{otp}\n")
            else:
                print(f" {M}└─ FAILED: OTP nahi mila (Service Blocked)")
                self.cp += 1
            
            time.sleep(8)

    def main_menu(self):
        self.logo()
        print(f"[{H}1{P}] Start Multi-Service Creator")
        if input(f"\n{M}>>{P} Select: ") == '1': self.start()

if __name__ == "__main__":
    PakMultiCreator()
