# -*- coding: utf-8 -*-
import scrapy


class GensunSpider(scrapy.Spider):
    name = 'gensun'
    allowed_domains = ['gensun.org']
    # 在浏览器里查看网页源代码，可查找到：
    # var q = "篠崎愛";
    # var pid = "1049291";
    # 使用 pid代替q，如下代码所示：
    start_urls = ['https://gensun.org/pid/1049291']
    # start_urls = ['https://gensun.org/?q=篠崎愛']

    def parse(self, response):
        print(response.text)

