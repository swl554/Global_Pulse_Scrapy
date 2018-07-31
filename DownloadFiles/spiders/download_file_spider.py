import scrapy
from download_files.items import MyItem

class MySpider(scrapy.Spider):
    """docstring for MySpider."""
    name = 'myspider'
    start_urls = [
        "https://www.reddit.com/r/programming"
    ]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        for selector in response.xpath("//h2/text()").extract():
            item = MyItem()
            item['title'] = selector
            yield(item)
