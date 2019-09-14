# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class FeixiaohaoSpider(scrapy.Spider):
    name = 'feixiaohao'
    allowed_domains = ['feixiaohao.com']
    start_urls = ['http://feixiaohao.com/']

    def parse(self, response):
        responseTest=response.text
        soup = BeautifulSoup(responseTest, 'lxml')
        print(soup.prettify())