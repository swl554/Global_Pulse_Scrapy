# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class JsonSpider(CrawlSpider):
    name = 'jsonspider'
    allowed_domains = []
    start_urls = ['https://archive.ics.uci.edu/ml/machine-learning-databases/00410/']

    rules = (
        Rule(LinkExtractor(allow = ".json") , callback = "parse_json"),
    )

#restrict_xpaths = "//*[contains(@href,'.json')]"
    def parse_json(self, response):
        print(response.url)
        json_data = json.loads(response.body_as_unicode())
        #json_data=open(links[0].url).read()
        #data = json.loads(json_data)
        print(json_data)
