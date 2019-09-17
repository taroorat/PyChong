# -*- coding: utf-8 -*-
import scrapy
from PyChong.items import MeituluItem

class MeituluSpider(scrapy.Spider):
    name = 'meitulu'
    allowed_domains = ['meitulu.com','ttsqgs.com']
    # start_urls = ['https://mtl.ttsqgs.com/images/img/2771/6.jpg']
    start_urls = ['https://www.meitulu.com/search/篠崎愛']

    def parse(self, response):
        # print(response)
        for url in response.xpath("//p[@class='p_title']").re('<p class="p_title"><a href="(.*)" target="_blank">.*</a></p>'):
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_images_url)

    def parse_images_url(self,response):
        print(response.xpath("//title"))
        img_urls = response.xpath("//center//img").re('<img src="(.*)" alt=.* class="content_img">')
        item = MeituluItem(image_urls=img_urls)
        yield item

    # def parse_images(self,response):
    #
    #     print(response.text)
