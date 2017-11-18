# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TesttestItem(scrapy.Item):
    # define the fields for your item here like:
    special = scrapy.Field()
    date = scrapy.Field()
    name = scrapy.Field()
    size = scrapy.Field()
    rate = scrapy.Field()
    types = scrapy.Field()
    details = scrapy.Field()
    pass

