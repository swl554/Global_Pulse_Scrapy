# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
import scrapy

class LinkItem(scrapy.Item):
    # define the fields for your item here like:
    # the source URL
    url_from = scrapy.Field()
    # the destination URL
    url_to = scrapy.Field()
