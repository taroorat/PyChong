# -*- coding: utf-8 -*-
import scrapy
from PyChong.items import MeituluItem

class MeituluSpider(scrapy.Spider):
    name = 'meitulu'
    girl = '篠崎愛'
    allowed_domains = ['meitulu.com','ttsqgs.com']
    # start_urls = ['https://mtl.ttsqgs.com/images/img/2771/6.jpg']
    start_urls = ['https://www.meitulu.com/search/%s'%(girl)]

    def parse(self, response):
        # print(response)
        for url in response.xpath("//p[@class='p_title']").re('<p class="p_title"><a href="(.*)" target="_blank">.*</a></p>'):
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_images)

    def parse_images(self,response):
        # path=response.xpath("//title").re('<title>(.*)</title>')[0]
        # path='mest'
        url_split=response.xpath("//center//img/@src").extract_first().split('1.jpg')
        img_urls=[]
        for i in range(200):
            # 初始url名称
            url_name = url_split[0]
            url_name=url_name+str(i)+'.jpg'
            # url list
            img_urls.append(url_name)
        item = MeituluItem(image_urls=img_urls)
        yield item

