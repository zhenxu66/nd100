# -*- coding: utf-8 -*-
import scrapy
import numpy as np
import datetime
from scrapy.http import Request
from urllib import parse
from nd100.items import Nd100Item
from scrapy.loader import ItemLoader

import re


class nd100listSpider(scrapy.Spider):
    name = 'nd100list'
    #allowed_domains = ['www.cnbc.com/'] this will allow urls beyond the basic start url
    base_url = 'http://www.cnbc.com/'

    start_urls = ['https://www.cnbc.com/nasdaq-100/']
    #start_urls = ['https://www.cnbc.com/']



    def parse(self, response):
        #yield scrapy.Request(self.base_url + 'nasdaq-100/', callback=self.parse)
        #Nd100Item_result = Nd100Item()


        # Extract information inside each page
        # using css to extract



        urls = response.css(".first.text  a::attr(href)").extract()
        symbols = response.css(" .first.text  a::text").extract()

        #names = response.css(".data.quoteTable tbody tr td:nth-of-type(2)").extract()  #only return empty list
        for i in np.arange(len(urls)):
            url = "http:"+urls[i]
            symbol = symbols[i]
            #Nd100Item_result["url"] = url
            #Nd100Item["name"] = name
            #Nd100Item_result["symbol"] = symbols[i]
            yield Nd100Item_result  # pass to item, and pipelines detect items
            #https://apps.cnbc.com/view.asp?symbol=AAPL.O&uid=stocks/summary


            #yield scrapy.Request('https://apps.cnbc.com/view.asp?symbol='+symbol + ".O&uid=stocks/summary", meta={'item_url': url, 'item_symbol':symbol},
                                 #callback=self.parse_detail)

        pass



    def parse_detail(self, response):
        Nd100Item_result = Nd100Item()

        desc = response.css("#descShort::text").extract_first()
        Nd100Item_result["url"] = response.meta['item_url']
        Nd100Item_result["symbol"] = response.meta['item_symbol']
        Nd100Item_result["descShort"] = desc
        yield Nd100Item_result  # pass to item
        pass
