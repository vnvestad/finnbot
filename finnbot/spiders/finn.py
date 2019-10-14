# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from finnbot.items import Ad, RealestateHome
import re

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
            id = int(response.css('span[data-adid]::attr(data-adid)').get())
        )
        ad['item'] = RealestateHome(
            estimated_value = price2int(response.css('span:contains("Prisantydning") + span::text').get()),
            no_of_bedrooms = response.css('dt:contains("Soverom") + dd::text').get(),
            ownership_type = response.css('dt:contains("Eieform") + dd::text').get(),
            plot_area = response.css('dt:contains("Tomteareal") + dd::text').get(),
            property_type = response.css('dt:contains("Boligtype") + dd::text').get(),
            size_gross = response.css('dt:contains("Bruttoareal") + dd::text').get(),
            size_primary = response.css('dt:contains("Primærrom") + dd::text').get(),
            size_usable = response.css('dt:contains("Bruksareal") + dd::text').get(),
            common_costs = price2int(response.css('dt:contains("Felleskost/mnd.") + dd::text').get())
        )
        yield ad

def price2int(price):
    return int("".join(re.findall(r'\d', price))) if price else None