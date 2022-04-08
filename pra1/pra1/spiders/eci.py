import scrapy
import json
import datetime
from pra1.items import eciItem


class EciSpider(scrapy.Spider):
    name = 'eci'
    allowed_domains = ['elcorteingles.com']
    start_urls = ['http://elcorteingles.com/']

    start_urls = ["https://www.elcorteingles.es/moda-hombre/ropa/"]

# we need to search for: 
# parent tag -> products-list
# class products_list-item -> span data-json
    # class = product_link
    
    def parse(self, response):

        default_url = "https://elcorteingles.es"
        # TO-DO: extract.pop........
        raw_json = response.xpath("//*[@class='products_list-item']/span/@data-json").extract()
        clean_json = [json.loads(i) for i in raw_json]
        

        id = [(field["id"]) for field in clean_json]
        name = [(field["name"]) for field in clean_json]
        brand = [(field["brand"]) for field in clean_json]
        category = [(field["category"]) for field in clean_json]
        price = [float(field["price"]["o_price"]) for field in clean_json]
        price_discount = [float(field["price"]["f_price"]) for field in clean_json]
        discount = [float(field["price"]["discount"]) for field in clean_json]
        perc_discount = [float(field["price"]["discount_percent"]) for field in clean_json]

        
        for i in zip(id, name, brand, category, price, price_discount, discount, perc_discount):
            item = eciItem(date = datetime.datetime.now().strftime('%Y-%m-%d'), id_product = i[0], name = i[1],
                    brand = i[2], category = i[3], price = i[4], 
                       price_discount = i[5], discount = i[6], perc_discount = i[7])

            yield item