# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exporters import JsonLinesItemExporter


class MyPipeline(object):
    def __init__(self):
        self.file = open("UCI_Data.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

'''
class JsonPipeline(object):
    def __init__(self):
        self.file = open("result_data.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class CsvPipeline(object):
    def __init__(self):
        self.file = open("result_data.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, unicode)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finishing_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return(item)

    def create_valid_csv(self, item):
        for key, value in item.items():
            is_string = (isinstance(value,basestring))
            if (is_string and ("," in value.encode('utf-8'))):
                item[key] = "\""+value+"\""
'''
