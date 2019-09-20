# -*- coding: utf-8 -*-

BOT_NAME = 'PyChong'

SPIDER_MODULES = ['PyChong.spiders']
NEWSPIDER_MODULE = 'PyChong.spiders'

# LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'WARNING'
# LOG_FILE = 'D:\\PycharmProjects\\logs\\log.txt'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 0.2
ITEM_PIPELINES = {
   # 'PyChong.pipelines.PychongPipeline': 300,
   # 'PyChong.pipelines.FeiXiaoHaoMysqlPipeline': 299,
   'PyChong.pipelines.MeituluImagesPipeline': 1,
   # 'PyChong.pipelines.SbiqugeCrawlspiderPipeline':1,
   # 'PyChong.pipelines.QuanshuwangCrawlspiderPipeline': 1,
}

#设置图片下载路径
IMAGES_STORE = 'D:\PycharmProjects\imgs\meitulu'
# IMAGES_STORE = '/Users/handsomechief/PycharmProjects3/images/meitulu'
# 过期天数
IMAGES_EXPIRES = 90  #90天内抓取的都不会被重抓
