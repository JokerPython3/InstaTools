import requests
import string
import random
from user_agent import generate_user_agent as e
import json,threading
a=0
def S1():
 global a
 ty= 263014407
 id = 361365133
 
 c = "".join(random.choices(string.ascii_letters + string.digits, k=32))
 
 headers = {
     'x-fb-lsd': c,
 
 }
 
 data = {
     'lsd': c,
     'variables':json.dumps({"id": int(random.randrange(ty, id)), "render_surface": "PROFILE"}),
     'doc_id': '28149645878012614',
 }
 
 try:
  r = requests.post('https://www.instagram.com/graphql/query',  headers=headers, data=data).json()
 
  a+=1
  oo=r['data']['user']['username']
  fol=r['data']['user']['follower_count']
  print(f'[=]{a}-User: {oo} | follower: {fol}')
  with open('S1.txt','a') as yy:
   yy.write(oo+'\n')
 except:
  pass
while True:
 for io in range(10):
  threading.Thread(target=S1).start()
