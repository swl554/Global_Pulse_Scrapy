import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


#process = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#})
process = CrawlerProcess()

process.crawl(link_extractor)
process.start()

def main():
    logging.basicConfig(filename='main.log', format="%(asctime)s%(levelname)s:%(message)s", level=logging.INFO)

if __name__=='__main__':
    main()
