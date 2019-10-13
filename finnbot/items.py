# Items reflect the structure of the official API, 
# e.g. https://www.finn.no/api/static/preview/ad/realestate-homes.xml

import scrapy


class Ad(scrapy.Item):
    id = scrapy.Field()
    item = scrapy.Field()

class RealestateHome(scrapy.Item):
    estimated_value = scrapy.Field()