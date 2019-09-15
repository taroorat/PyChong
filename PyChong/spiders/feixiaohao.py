# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json

class FeixiaohaoSpider(scrapy.Spider):
    name = 'feixiaohao'
    allowed_domains = ['feixiaohao.com','bqiapp.com']
    start_urls = ['https://dncapi.bqiapp.com/api/coin/web-coinrank?page=1&type=-1&pagesize=5&webp=1']

    def parse(self, response):
        responseData = []
        for data in response.css('p').re('<p>(.*)</p>'):
            responseData=data
            responseData = json.loads(responseData)
            # print(json.dumps(responseData,indent=4))
            print(type(responseData['data']))
            for data in responseData['data']:
                print(data)




