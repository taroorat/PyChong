# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from PyChong.items import MeituluItem

class CrawlmeituluSpider(CrawlSpider):
    name = 'CrawlMeitulu'
    allowed_domains = ['meitulu.com','ttsqgs.com']
    # start_urls = ['http://meitulu.com/t/nvshen/']
    start_urls = ['http://meitulu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'item/\d+?'), callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=r't/nvshen/\d+?'), follow=True),
    )

    def parse_item(self, response):
        image_list = response.xpath('//center/img/@src')
        print(response)
        title="test"
        # print(image_list)
        img_urls = []
        for image in image_list:
            # print(image)
            image_url=image.re('(.*)')[0]
            # print(image_url)
            img_urls.append(image_url)
        url=response.xpath('//div[@class="boxs"]//a/@href').extract_first()
        print(url)
        yield scrapy.Request(url=url, callback=self.parse_item,meta={'title' : title})
        item = MeituluItem(image_urls=img_urls,title=response.meta['title'])
        yield item
