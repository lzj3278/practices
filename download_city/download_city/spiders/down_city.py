# -*- coding:utf-8 -*-

from scrapy import Spider
from scrapy_splash import SplashRequest
import re


class Down_City(Spider):
    name = 'autohome'
    allowed_domains = ['www.autohome.com.cn']
    start_urls = [
        "https://www.autohome.com.cn/Violation/"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse_item, args={
                'wait': 0.5, 'html': 1, })

    def parse_item(self, response):
        item_province = response.xpath('./*//div[@id="provinceList"]/dl/dd/a/text()').extract()
        item_province_id = response.xpath('./*//div[@id="provinceList"]/dl/dd/@provinceid').extract()
        list_privonce = zip(item_province_id, item_province)
        for i, j in list_privonce:
            print(i, j)


class Ajax_Test(Spider):
    name = 'ajax'
    allowed_domains = ['juicystudio.com']
    start_urls = [
        "http://juicystudio.com/experiments/ajax/index.php"
    ]

    def start_requests(self):
        script = """
            function main(splash)
                splash:runjs("$('#fact').click()")
                splash:wait(1)
            end
        """
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse_item, args={
                'wait': 0.5, 'lua_source': script, })

    def parse_item(self, response):
        item_text = response.xpath('./*//p[@id="update"]/text()').extract()
        print(item_text)
