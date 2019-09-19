# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
url="http://youtube.com/watch?v=9bZkp7q19f0"
proxies={}
proxies={'http':'http://127.0.0.1:1087'}

response=requests.get(url,headers=headers,proxies=proxies,timeout=1)
responseTest=response.text
print(responseTest)
if response.status_code == 200:
    soup=BeautifulSoup(responseTest,'lxml')
    #select css选择器，calss. id#
    print(soup.select('.reader_crumb a')[2].get_text())
    print(soup.select('.title_txtbox')[0].get_text())
    for content in soup.find_all('p'):
        print(content.get_text())
else :
    print("error code: %d"% response.status_code)

