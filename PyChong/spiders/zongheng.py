# -*- coding: utf-8 -*-
import scrapy


class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['zongheng.com']
    start_urls = ['http://book.zongheng.com/chapter/672340/36898237.html']

    def parse(self, response):
        # print(response.css('p').re('<p>(.*)</p>'))
        # print(response.text)
        nextUrl=""
        for content in response.css('p').re('<p>(.*)</p>'):
            with open ("../files/test.txt","a") as f:
                f.write("\n")
                f.write(content)
            print(content)
        for nextUrl in response.css('div.chap_btnbox').re('<a href="(.*)" class=.*\}\'>.*</a>'):
            print(nextUrl)

        yield scrapy.Request(url=nextUrl, callback=self.parse)

