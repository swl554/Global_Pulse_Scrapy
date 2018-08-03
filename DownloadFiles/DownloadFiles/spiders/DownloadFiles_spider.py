import scrapy
import logging
from DownloadFiles.items import MyItem
from DownloadFiles.pipelines import MyPipeline
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.options import Options
import os

class MySpider(scrapy.Spider):
    """
    Let's try a simple spider that downloads one json file from UCI machinelearning database
    """

    logging.basicConfig(filename='DownloadFiles.log', format="%(asctime)s%(levelname)s:%(message)s", level=logging.INFO)

    name = 'myspider'
    start_urls = [
        "https://archive.ics.uci.edu/ml/machine-learning-databases/00410/"
    ]



    def parse(self, response):
        self.logger.info('Able to get response from %s', response.url)
        # set up webdriver
        chop = webdriver.ChromeOptions()
        chop.add_extension(os.path.abspath('AdBlock_v3.32.0.crx'))
        browser = webdriver.Chrome(chrome_options = chop)
        #item = MyItem()
        #item['first_items'] = response.xpath("//*[contains(@href,'.json')]").extract()
        #return(item)
        browser.get(response.url)
        browser.find_element_by_xpath("//*[contains(@href,'.json')]").click()
        #driver.find_element_by_id("mas-resultados-fresadoras").click()
        #yield
