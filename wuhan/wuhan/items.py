# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WuhanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    yiqingdonginstance = scrapy.Field()

    yiqing_sheet = scrapy.Field()