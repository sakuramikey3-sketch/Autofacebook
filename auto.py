import os, sys, time, re, random, requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

#--- Warna (Colors) ---
H = "\x1b[38;5;46m"  # Hara
M = "\x1b[38;5;196m" # Laal
P = "\x1b[38;5;231m" # Safaid
A = "\x1b[38;5;248m" # Abu

class PakFinalCreator:
    def __init__(self):
        self.ses = requests.Session()
        self.ok = 0
        self.cp = 0
        self.loop = 0
        self.names_boys = ['Muhammad Ali', 'Hamza Khan', 'Zaid Sheikh', 'Usman Butt', 'Bilal Arshad', 'Hassan Raza', 'Khurram Shahzad', 'Fahad Malik']
        self.names_girls = ['Ayesha Bibi', 'Sana Malik', 'Fatima Zahra', 'Zainab Khan', 'Mariam Jameel', 'Hira Mani', 'Sara Ahmed']
        self.main_menu()

    def logo(self):
        os.system('clear')
        print(f"""{H}
  ____   _    _  __  _____ ____  
 |  _ \ / \  | |/ / |  ___| __ ) 
 | |_) / _ \ | ' /  | |_  |  _ \ 
 |  __/ ___ \| . \  |  _| | |_) |
 |_| /_/   \_\_|\_\ |_|   |____/ 
 {P}------------------------------------------
 {M}>> {P}Region  : Pakistan (2025 Optimized)
 {M}>> {P}Feature : Auto-Email + Auto-DP
 {P}------------------------------------------""")

    def get_ua(self):
        # Latest High-End Device UA for Pakistan
        model = random.choice(['SM-S911B', 'V2227A', 'RMX3686', 'Infinix X6833', 'Tecno LH7n'])
        v = random.randint(11, 14)
        chrome = f"{random.randint(115, 130)}.0.{random.randint(5000, 6500)}.{random.randint(10, 150)}"
        return f"Mozilla/5.0 (Linux; Android {v}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36"

    def main_menu(self):
        self.logo()
        print(f"[{H}1{P}] Create Male Accounts")
        print(f"[{H}2{P}] Create Female Accounts")
        print(f"[{M}0{P}] Exit")
        
        opt = input(f"\n{M}>>{P} Option: ")
        if opt in ['1','2']:
            self.gender = 'male' if opt == '1' else 'female'
            self.start_creation()
        else: exit()

    def upload_dp(self, ua, cookies):
        try:
            if not os.path.exists('photos') or not os.listdir('photos'):
                return # Agar photos nahi hain to skip karein
            
            img_name = random.choice(os.listdir('photos'))
            img_path = os.path.join('photos', img_name)
            
            # Use mbasic for faster upload
            res = self.ses.get("https://mbasic.facebook.com/profile_picture/", headers={'User-Agent': ua}, cookies=cookies)
            soup = bs(res.text, 'html.parser')
            form = soup.find('form', method='post')
            if not form: return
            
            url = form['action']
            data = {
                'fb_dtsg': soup.find('input', {'name': 'fb_dtsg'})['value'],
                'jazoest': soup.find('input', {'name': 'jazoest'})['value'],
                'submit': 'Set as Profile Picture'
            }
            files = {'pic': open(img_path, 'rb')}
            self.ses.post(url, data=data, files=files, headers={'User-Agent': ua}, cookies=cookies)
            print(f" {H}└─ DP Uploaded Successfully!{P}")
        except: pass

    def start_creation(self):
        limit = int(input(f"{M}>>{P} Kitni IDs?: "))
        delay = int(input(f"{M}>>{P} Delay (seconds): "))
        
        for _ in range(limit):
            self.loop += 1
            ua = self.get_ua()
            name = random.choice(self.names_boys if self.gender == 'male' else self.names_girls)
            
            # Simple Email System
            email = f"pak{random.randint(100,999)}{random.getrandbits(16)}@1secmail.com"
            password = f"Pak@{random.randint(111,999)}#"
            
            print(f"\n{H}[{self.loop}] {P}Creating: {name}")
            print(f" {A}└─ Email: {email}")

            try:
                # FB Registration Process (Simplified logic)
                reg_url = "https://m.facebook.com/reg/submit/"
                payload = {
                    'firstname': name.split()[0],
                    'lastname': name.split()[1],
                    'reg_email__': email,
                    'reg_passwd__': password,
                    'sex': '2' if self.gender == 'male' else '1',
                    'birthday_day': str(random.randint(1,28)),
                    'birthday_month': str(random.randint(1,12)),
                    'birthday_year': str(random.randint(1995,2003))
                }
                
                # Request
                response = self.ses.post(reg_url, data=payload, headers={'User-Agent': ua})
                cookies = self.ses.cookies.get_dict()

                if "c_user" in cookies:
                    print(f" {H}└─ Status: SUCCESS (OK)")
                    self.ok += 1
                    open('pak_ok.txt', 'a').write(f"{email}|{password}|{cookies}\n")
                    self.upload_dp(ua, cookies)
                elif "checkpoint" in cookies:
                    print(f" {M}└─ Status: CHECKPOINT (CP)")
                    self.cp += 1
                else:
                    print(f" {A}└─ Status: FAILED (Spam Block)")

            except Exception as e:
                print(f" {M}└─ Connection Error!")

            print(f"{A}Waiting {delay}s... (Airplane Mode ON/OFF if needed){P}")
            time.sleep(delay)

        print(f"\n{H}Process Completed! OK: {self.ok} | CP: {self.cp}")

if __name__ == "__main__":
    PakFinalCreator()
    