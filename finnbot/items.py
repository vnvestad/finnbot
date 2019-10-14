# Items reflect the structure of the official API, 
# e.g. https://www.finn.no/api/static/preview/ad/realestate-homes.xml

import scrapy


class Ad(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()

    item = scrapy.Field()

class RealestateHome(scrapy.Item):
    advertiser_reference = scrapy.Field()

    cadastres_cadastral_unit_number = scrapy.Field()
    cadastres_property_unit_number = scrapy.Field()
    cadastres_county_number = scrapy.Field()

    change_of_ownership_insurance = scrapy.Field()
    construction_year = scrapy.Field()
    energy_label = scrapy.Field()
    energy_label_color_code = scrapy.Field()
    general_text = scrapy.Field()
    no_of_bedrooms = scrapy.Field()
    ownership_type = scrapy.Field()
    plot_area = scrapy.Field()
    plot_owned = scrapy.Field()
    property_type = scrapy.Field()
    size_gross = scrapy.Field()
    size_primary = scrapy.Field()
    size_usable = scrapy.Field()
    viewings = scrapy.Field()

    estimated_value = scrapy.Field()
    loan_fare = scrapy.Field()
    community_tax = scrapy.Field()
    tax_value = scrapy.Field()
    common_costs = scrapy.Field()
