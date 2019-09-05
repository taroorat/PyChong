# -*- coding: utf-8 -*-
import scrapy


class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://book.zongheng.com/chapter/672340/36898237.html']

    def parse(self, response):
        print(response.css('p').extract_first())

