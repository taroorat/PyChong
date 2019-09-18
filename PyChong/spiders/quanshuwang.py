# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from PyChong.items import QuanshuwangCrawlspiderItem

class QuanshuwangSpider(CrawlSpider):
    name = 'quanshuwang'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://quanshuwang.com/']

    rules = (
        Rule(LinkExtractor(allow="/\d+?/\d+?"),callback='parse_item',follow=False),
    )

    def parse_item(self, response):
        chap_list = response.xpath('.//*[@class="clearfix dirconone"]//li')
        # print(chap_list)
        id=0
        for chapter in chap_list:
            id=id+1
            novel_name = response.xpath('//div[@class="dirtitone"]/h2/text()').extract_first()
            chapter_name = chapter.xpath('./a/text()').extract_first()
            chapter_link = chapter.xpath('./a/@href').extract_first()
            if chapter_name:
                # print(novel_name,chapter_link,chapter_name)
                item = QuanshuwangCrawlspiderItem(id=id,chapter_title=chapter_name, novel_name=novel_name)
                url = chapter_link
                request = scrapy.Request(url=url, callback=self.parse_body)
                # print(request,url)
                request.meta['key'] = item
                # print(item)
                yield request

    def parse_body(self, response):
        item = response.meta['key']
        # print(item)
        # response.xpath('//div[@id="content"]/text()').getall() 为list列表
        contents=''.join(response.xpath('//div[@class="mainContenr"][@id="content"]/text()').getall())

        # print(contents,'\n','\n','\n','\n','\n')
        item['contents'] = contents
        # print(item)
        yield item