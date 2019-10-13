# -*- coding: utf-8 -*-
import scrapy


class FinnSpider(scrapy.Spider):
    name = 'finn'
    allowed_domains = ['finn.no']
    start_urls = ['http://finn.no/']

    def parse(self, response):
        pass
