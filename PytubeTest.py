import urllib.request
from pytube import YouTube

### 设置代理（没啥用）
# proxy_addr = 'http://127.0.0.1:1087'
# proxy = urllib.request.ProxyHandler({'http':proxy_addr})
#
# opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)


####### python 选3.5.3可用，当前3.7 报证书错误（mac下）
####### widows3.7下可正常使用
url='https://youtube.com/watch?v=9bZkp7q19f0'
yt = YouTube(url)
print(yt.streams.all())
