# -*- coding: utf-8 -*-
import requests
# r=requests.get('https://www.douban.com/',params={'q': 'python', 'cat': '1001','chartset':'utf-8'})
# print(r.status_code)
# print(r.text)
#r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': '429835306@qq.com', 'form_password': '123456'})
print(r.text)
params = {'form_email': '429835306@qq.com', 'form_password': '123456'}
r = requests.post('https://accounts.douban.com/login', json=params)
upload = {'file': open('test.txt', 'rb')}

r = requests.post('https://accounts.douban.com/login', files=upload)

print(r.cookies['ts'])

cs = {'token': '12345', 'status': 'working'}
r = requests.post('www....',cookies=cs,timeout=2.5)
