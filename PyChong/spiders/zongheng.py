# -*- coding: utf-8 -*-
import scrapy


class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://zongheng.com/']

    def parse(self, response):
        pass
