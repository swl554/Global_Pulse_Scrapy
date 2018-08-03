# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class JsonSpider(CrawlSpider):
    name = 'jsonspider'
    allowed_domains = []
    start_urls = [
    'https://archive.ics.uci.edu/ml/machine-learning-databases/00410/',
    'https://finance.yahoo.com/quote/FDA.F/history?p=FDA.F',
    'https://www.ncdc.noaa.gov/ghcn/comparative-climatic-data',
    'http://usda.mannlib.cornell.edu/MannUsda/viewDocumentInfo.do;jsessionid=F154BA78C7C50C021C8CA924EDB72FD5?documentID=1066',
    ]


    rules = (
        Rule(LinkExtractor(allow = ".json") , callback = "parse_json"),
        Rule(LinkExtractor(allow = ".csv"), callback = "parse_csv"),
        Rule(LinkExtractor(allow = ".dat"), callback = "parse_dat"),
        Rule(LinkExtractor(allow = ".txt"), callback = "parse_txt"),
    )

    def parse_json(self, response):
        print("we got json")
        print(response.url)
        json_data = json.loads(response.body_as_unicode())
        #json_data=open(links[0].url).read()
        #data = json.loads(json_data)

    def parse_csv(self, response):
        print("we got csv")
        print(response.url)

    def parse_dat(self, response):
        print("we got dat")
        print(response.url)
        ph_data = urlopen(response.url).read()
        print(ph_data)
    #    ph_dict = {}
    #    ph_dict["item1"] = ph_data
    #    yield ph_dict

    def parse_txt(self, response):
        print("we got txt")
        print(response.url)
