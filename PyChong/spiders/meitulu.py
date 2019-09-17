# -*- coding: utf-8 -*-
import scrapy


class MeituluSpider(scrapy.Spider):
    name = 'meitulu'
    allowed_domains = ['meitulu.com']
    start_urls = ['https://www.meitulu.com/search/篠崎愛']

    def parse(self, response):
        # print(response.text)
        url=''
        for url in response.xpath("//p[@class='p_title']").re('<p class="p_title"><a href="(.*)" target="_blank">.*</a></p>'):
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_images)

    def parse_images(self,response):
        print(response.xpath("//title"))
        print(response.xpath("//center//img"))

