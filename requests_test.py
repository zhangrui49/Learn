# -*- coding: utf-8 -*-
import requests
r=requests.get('https://www.douban.com/',params={'q': 'python', 'cat': '1001','chartset':'utf-8'})
print(r.status_code)
print(r.text)