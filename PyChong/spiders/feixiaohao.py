# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json

class FeixiaohaoSpider(scrapy.Spider):
    name = 'feixiaohao'
    allowed_domains = ['feixiaohao.com','bqiapp.com']
    start_urls = ['https://dncapi.bqiapp.com/api/v2/ranking/coinvol?per_page=100&page=1&sort=vol_m&webp=1']

    def parse(self, response):
        responseData = []
        for data in response.css('p').re('<p>(.*)</p>'):
            responseData=data
        print(json.loads(responseData))

        # soup = BeautifulSoup(responseTest, 'lxml')
        # print(soup.prettify())

