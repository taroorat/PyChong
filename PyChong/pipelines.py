# -*- coding: utf-8 -*-
import pymysql

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
        self.cursor.execute(self.sql, (item['rank'],item['name']))
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