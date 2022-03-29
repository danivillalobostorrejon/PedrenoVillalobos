import scrapy

class eciItem(scrapy.Item):

    date = scrapy.Field()
    id_product = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    #colors = scrapy.Field()