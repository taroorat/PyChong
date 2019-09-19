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
        # print(response)
        title=response.xpath('//title/text()').re("(.*)P\]_.*")[0]
        print(title)
        # print(image_list)
        img_urls = []
        for image in image_list:
            # print(image)
            image_url=image.re('(.*)')[0]
            # print(image_url)
            img_urls.append(image_url)
        url_short_list = response.xpath('//a[@class="a1"]/@href').extract()
        url=response.xpath('//ul[@class="img"]//a/@href').extract_first()
        # 扩展url为3个
        url_list=[]
        url_list.append(url)
        for url in url_short_list:
            url=response.urljoin(url)
            url_list.append(url)
        # url遍历
        for url in url_list:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_item,meta={'title' : title})
        # 解决title错误
        item = MeituluItem(image_urls=img_urls, title=title)
        yield item
