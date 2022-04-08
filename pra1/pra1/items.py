# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class eciItem(scrapy.Item):

    date = scrapy.Field()
    id_product = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    price_discount = scrapy.Field()
    discount = scrapy.Field()
    perc_discount = scrapy.Field()
