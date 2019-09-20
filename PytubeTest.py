import requests
from pytube import YouTube
from bs4 import BeautifulSoup
import re
import os
import urllib

search_query='Fancam+Nancy'

def get_search_short_url():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    url = "https://www.youtube.com/results?search_query=%s"%(search_query)
    proxies = {}
    proxies = {'http': 'http://127.0.0.1:1087'}
    response = requests.get(url, headers=headers, proxies=proxies, timeout=1)
    responseTest = response.text
    if response.status_code == 200:
        soup = BeautifulSoup(responseTest, 'lxml')
        # select css选择器，calss. id#
        # print(soup.prettify())
        print(soup.select('#img-preload img'))
        short_src_list=[]
        for src in soup.select('#img-preload img'):
            # print(str(src))
            short_src= re.match(r'.*"https://i\.ytimg\.com/vi/(.*)/hqdefault\.jpg.*', str(src))
            short_src_list.append(short_src.group(1))
        return short_src_list


def download_vedio():
    path = 'D:\PycharmProjects\\vedios\pytube\%s'%(search_query)
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    short_url_list=get_search_short_url()
    for short_url in short_url_list:
        print(short_url)
        url = 'https://www.youtube.com/watch?v=xBbfRL9Aiqo'
        url = 'https://www.youtube.com/watch?v=' + short_url
        yt = YouTube(url)
        # for stream in (yt.streams.filter(subtype='mp4').all()):
        #     print(stream)
        try:
            yt.streams.get_by_itag(137).download(path)
        except Exception  as e:
            print(e)


if __name__ == '__main__':
    download_vedio()
