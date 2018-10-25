# -*- coding: utf-8 -*-
import scrapy
import numpy as np
import datetime
from scrapy.http import Request
from urllib import parse
from nd100.items import Nd100Item
from scrapy.loader import ItemLoader
from nd100.models import bs_extract

import re

#add net income growth

class nd100listSpider(scrapy.Spider):
    name = 'nd100detail2'
    base_url = 'http://www.cnbc.com/'
    start_urls = ['https://www.cnbc.com/nasdaq-100/']


    def parse(self, response):
        urls = response.css(".first.text  a::attr(href)").extract()
        symbols = response.css(" .first.text  a::text").extract()
        #names = response.css(".data.quoteTable tbody tr").extract()

        for i in np.arange(len(urls)):
            url = "http:"+urls[i]
            symbol = symbols[i]
            yield scrapy.Request('https://apps.cnbc.com/view.asp?symbol='+symbol + ".O&uid=stocks/summary", meta={'item_url': url, 'item_symbol':symbol},
                                 callback=self.parse_detail)
        pass


    def parse_detail(self, response):
        Nd100Item_result = Nd100Item()
        descShort = response.css("#descShort::text").extract_first()
        descLong = response.css("#descLong::text").extract_first()
        CEO = response.css(".drkr::text").extract_first()
        if len(response.css(".drkr1::text").extract()) >= 4: # US address: street city state country with zipcode
            address = response.css(".drkr::text").extract()[1] + ', ' + response.css(".drkr1::text").extract()[0] + ', ' +\
                      response.css(".drkr1::text").extract()[1] + ', ' + response.css(".drkr1::text").extract()[2] + ', ' +\
                      response.css(".drkr1::text").extract()[3]
        else:    # EU address with less information not sure if I can use extract_second()
            address = response.css(".drkr::text").extract()[1] + ', ' + response.css(".drkr1::text").extract()[0] + ', ' +\
                      response.css(".drkr1::text").extract()[1] + ', ' + response.css(".drkr1::text").extract()[2]
        shares_out = response.css(".bold.aRit::text").extract()[0]
        inst_own = response.css(".bold.aRit::text").extract()[1]
        mark_cap = response.css(".bold.aRit::text").extract()[2]
        #GPM = response.css("#keyMeasures .moduleBox .floatWrapper::text").extract() # 5 module class
        NIGR_result = bs_extract.get_NIGR_dict(response.meta['item_symbol'])



        Nd100Item_result["url"] = response.meta['item_url']
        Nd100Item_result["symbol"] = response.meta['item_symbol']
        Nd100Item_result["descShort"] = descShort
        Nd100Item_result["descLong"] = descLong
        Nd100Item_result["CEO"] = CEO
        Nd100Item_result["address"] = address
        Nd100Item_result["shares_out"] = shares_out
        Nd100Item_result["inst_own"] = inst_own
        Nd100Item_result["mark_cap"] = mark_cap
        Nd100Item_result["NIGR_result"] = NIGR_result

        yield Nd100Item_result  # pass to item
        pass
