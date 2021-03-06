# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PychongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FeixiaohaoItem(scrapy.Item):
    # 定义需要的存储数据字段
    rank=scrapy.Field()
    name=scrapy.Field()

class MeituluItem(scrapy.Item):

    # ... other item fields ...
    title=scrapy.Field()
    path=scrapy.Field()
    image_urls = scrapy.Field()
    image_paths=scrapy.Field()

class SbiqugeCrawlspiderItem(scrapy.Item):
    id=scrapy.Field()
    contents=scrapy.Field()
    chapter_title = scrapy.Field()
    novel_name = scrapy.Field()

class QuanshuwangCrawlspiderItem(scrapy.Item):
    id=scrapy.Field()
    contents=scrapy.Field()
    chapter_title = scrapy.Field()
    novel_name = scrapy.Field()