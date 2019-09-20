import urllib.request
from pytube import YouTube

### 设置代理（没啥用）
# proxy_addr = 'http://127.0.0.1:1087'
# proxy = urllib.request.ProxyHandler({'http':proxy_addr})
#
# opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
# urllib.request.install_opener(opener)

# url https://www.youtube.com/watch?v=ECF4CQ8yABs&list=PLZI_M9ry4jeUz4r7lVdSUdpo2VTh5ntXQ
# url https://www.youtube.com/watch?v=uWZpy4vGbFQ
####### python 选3.5.3可用，当前3.7 报证书错误（mac下）
####### widows3.7下可正常使用

url='https://www.youtube.com/watch?v=uWZpy4vGbFQ'
yt = YouTube(url)
print(yt.streams.all())
