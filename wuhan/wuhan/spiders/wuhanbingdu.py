# -*- coding: utf-8 -*-
import scrapy
import json
from wuhan.items import WuhanItem

class WuhanbingduSpider(scrapy.Spider):
    name = 'wuhanbingdu'
    allowed_domains = ['voice.baidu.com']
    start_urls = ['http://voice.baidu.com/'+'/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab3']

    def parse(self, response):

        item = WuhanItem()

        content_list = response.xpath("//div[@id='viewport']//div[@id='main']")
        list_A = []
        if content_list == list_A:
            print('没有请求到数据')
        else:
            for amc in content_list:

                item['yiqingdonginstance'] = amc.xpath(".//div[@class='VirusSummarySix_1-1-192_ZRHUKw']//text()").extract_first()

                item['yiqing_sheet'] = amc.xpath(".//tr//td[@colspan='5']//tr//text()").extract_first()

                yield item



