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
    #colors = scrapy.Field()