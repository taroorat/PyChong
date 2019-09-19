# -*- coding: utf-8 -*-
import scrapy
from PyChong.items import MeituluItem

class MeituluSpider(scrapy.Spider):
    name = 'meitulu'
    girl = '新垣结衣'
    allowed_domains = ['meitulu.com','ttsqgs.com']
    # start_urls = ['https://mtl.ttsqgs.com/images/img/2771/6.jpg']
    start_urls = ['https://www.meitulu.com/search/%s'%(girl)]

    def parse(self, response):
        # print(response)
        # 变量list包含url和title，将title传送到request，在parse_images方法中的item添加title=response.meta['title']，
        # 在pipelines 中get_media_requests的方法里获取item['title']，再yield
        # 在 file_path中获取request.meta['title']
        for list in response.xpath("//p[@class='p_title']"):
            # print(list)
            url=list.xpath('./a/@href').extract_first()
            title=list.xpath('./a/text()').extract_first()
            # print(url,title)
            yield scrapy.Request(url=url, callback=self.parse_images,meta={'title' : title})


    def parse_images(self,response):

        url_split=response.xpath("//center//img/@src").extract_first().split('1.jpg')
        img_urls=[]
        for i in range(200):
            # 初始url名称
            url_name = url_split[0]
            url_name=url_name+str(i)+'.jpg'
            # url list
            img_urls.append(url_name)
        item = MeituluItem(title=response.meta['title'],image_urls=img_urls)
        # print(item)
        yield item


