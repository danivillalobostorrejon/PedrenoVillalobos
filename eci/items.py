import scrapy

class eciItem(scrapy.Item):

    date = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    colors = scrapy.Field()
    composition = scrapy.Field()
    sleeves = scrapy.Field()