# -*- coding: utf-8 -*-
import scrapy
from finnbot.items import Ad, RealestateHome

class FinnSpider(scrapy.Spider):
    name = 'finn'
    allowed_domains = ['finn.no']
    start_urls = ['https://www.finn.no/realestate/homes/search.html?filters=']

    def parse(self, response):
        ad_urls = response.css('div.ads__unit__content a::attr(href)').getall()
        for ad_url in ad_urls:
            yield response.follow(ad_url, callback=self.parse_ad)

        next_url = response.css('a[rel=next]::attr(href)').get()
        if next_url is not None:
            yield response.follow(next_url, callback=self.parse)

    def parse_ad(self, response):
        ad = Ad(
            id = response.css('span[data-adid]::attr(data-adid)').get()
        )
        ad['item'] = RealestateHome(
            estimated_value = int("".join(response.css('span:contains("Prisantydning") + span').re(r'\d')))
        )
        yield ad
