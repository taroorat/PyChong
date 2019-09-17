# -*- coding: utf-8 -*-
import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from PyChong.spiders.meitulu import MeituluSpider

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PychongPipeline(object):
    def process_item(self, item, spider):
        return item


class FeiXiaoHaoMysqlPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '192.168.10.133',
            'port': 3306,
            'user': 'test',
            'password': '123456',
            'database': 'feixiaohao',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['rank'], item['name']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into ValueRank(rank,name) values(%s,%s)
                """
            return self._sql
        return self._sql


class MeituluImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-2]+'-'+request.url.split('/')[-1]
        image_path=request.url.split('/')[-2]
        # file_dir=request.meta['xxx']
        file_name=MeituluSpider.girl
        return '%s/%s/%s' % (file_name,request.url.split('/')[-2],image_guid)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
