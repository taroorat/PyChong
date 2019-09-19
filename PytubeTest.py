import urllib.request
from pytube import YouTube

# proxy_addr = 'http://127.0.0.1:1087'
# proxy = urllib.request.ProxyHandler({'http':proxy_addr})
#
# opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)
# #输入要下载的视频的路径
# print(1)
####### python 选3.5.3可用，当前3.7 报证书错误
url='https://youtube.com/watch?v=9bZkp7q19f0'
yt = YouTube(url)
print(yt.streams.all())
