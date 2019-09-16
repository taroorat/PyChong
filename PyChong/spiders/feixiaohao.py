# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json
from PyChong.items import FeixiaohaoItem

class FeixiaohaoSpider(scrapy.Spider):
    name = 'feixiaohao'
    allowed_domains = ['feixiaohao.com','bqiapp.com']
    start_urls = ['https://dncapi.bqiapp.com/api/coin/web-coinrank?page=1&type=-1&pagesize=10&webp=1']

    def parse(self, response):
        for data in response.css('p').re('<p>(.*)</p>'):
            responseData=data
            responseData = json.loads(responseData)
            for item in responseData['data']:
                print(item['name'])
                name=item['name']
                item = FeixiaohaoItem(
                    name=name
                )
                yield item



