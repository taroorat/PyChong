# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from PyChong.items import SbiqugeCrawlspiderItem
import logging

class SbiqugeSpider(CrawlSpider):
    name = 'sbiquge'
    allowed_domains = ['sbiquge.com']
    start_urls = ['http://sbiquge.com/']
    rules = (
        Rule(LinkExtractor(allow="/\d+?_\d+?/"),callback='parse_item',follow=False),
    )

    def parse_item(self, response):
        chap_list = response.xpath('.//*[@class="listmain"]/dl/dd')
        id=0
        # logging.warning(response.xpath('//a/@href').extract())
        # logging.warning(response)
        for chapter in chap_list:
            id=id+1
            novel_name = chapter.xpath('//*[@id="book"]/div[1]/div/a[2]/text()').extract_first()
            chapter_name = chapter.xpath('./a/text()').extract_first()
            chapter_link = chapter.xpath('./a/@href').extract_first()
            # chapter_name 判断很重要，避免进入非小说目录
            if chapter_name:
                # print(novel_name,chapter_link,chapter_name)
                item = SbiqugeCrawlspiderItem(id=id,chapter_title=chapter_name, novel_name=novel_name)
                url = response.urljoin(chapter_link)
                request = scrapy.Request(url=url, callback=self.parse_body)
                # print(request,url)
                request.meta['key'] = item
                # print(item)
                # logging.warning("A                      +                    %s",request)
                yield request


    def parse_body(self, response):
        item = response.meta['key']
        # print(item)
        # response.xpath('//div[@id="content"]/text()').getall() 为list列表
        contents=''.join(response.xpath('//div[@id="content"]/text()').getall())
        item['contents'] = contents
        # print(item)
        yield item
