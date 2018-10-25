# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Nd100Item(scrapy.Item):
    # define the fields for your item here like:
    symbol = scrapy.Field()
    #name = scrapy.Field()
    url = scrapy.Field()
    descShort = scrapy.Field()
    descLong = scrapy.Field()
    CEO = scrapy.Field()
    address = scrapy.Field()
    shares_out = scrapy.Field()
    inst_own = scrapy.Field()
    mark_cap = scrapy.Field()
    NIGR_result = scrapy.Field() #new for nd100detail2.py
    pass

