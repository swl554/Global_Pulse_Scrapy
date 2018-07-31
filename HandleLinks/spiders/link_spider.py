import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from link_extractor.items import LinkExtractorItem

class link_extractor(CrawlSpider):
    name = "link_extractor"
    allowed_domains = ['fastfoodmenuprices.com']
    start_urls = ['https://www.fastfoodmenuprices.com/all-restaurants/']

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    # Method for parsing items
    def parse_items(self, response):
        # The list of items that are found on the particular page
        #items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        items = LinkExtractorItem()
        for link in links:
            item['url_from'] = response.url
            item['url_to'] = link.url
            items.append(item)

'''
        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = LinkExtractorItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)
        # Return all the found items
        #return items
'''
