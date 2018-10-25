# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class Nd100Pipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):  # initialize the DB Connection
        self.conn = mysql.connector.connect(user='root', password='gmw6504192658',
                                            host='127.0.0.1', database='nd100list', charset='utf8',
                                            use_unicode=True)
        self.cursor = self.conn.cursor()  # Database operation

    def process_item(self, item, spider):
        insert_sql = """
            insert into nd100list(symbol,url,descShort, descLong, CEO, address, shares_out, inst_own, mark_cap, NIGR_result)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

        """
        self.cursor.execute(insert_sql, (item['symbol'], item['url'],item['descShort'],item['descLong'],item['CEO'], item['address'], item['shares_out'],
                                         item['inst_own'], item['mark_cap'],item['NIGR_result']))
        self.conn.commit()
        return item