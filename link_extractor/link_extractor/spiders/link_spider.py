import scrapy


class QuotesSpider(scrapy.Spider):
    name = "link"

    def start_requests(self):
        urls = [
            'https://finance.yahoo.com/quote/FDA.F/history/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        print(page)
