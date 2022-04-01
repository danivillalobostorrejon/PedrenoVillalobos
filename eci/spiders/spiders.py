from http.client import responses
import scrapy
#from eci.items import eciItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy import linkextractors


class eciSpider(CrawlSpider):

    name = "eci"
    allowed_domains = ["elcorteingles.es"]


    start_url = ["https://www.elcorteingles.es/moda-hombre/ropa/"]

# we need to search for: 
# parent tag -> products-list
# class products_list-item -> span data-json
    # class = product_link
    
    def parse_price(self, response):
        # TO-DO: extract.pop........
        good_one = response.xpath("//*[@class='products_list-item']/span").extract()

        price = good_one["price"]["o_price"]
        # Sacar lista de precios de los diferentes elementos

        lst_price = [float(flat_price.extract().replace(',','.').strip())
                    for flat_price in price]

        return good_one

    # def parse_discount(self, info_clothing_dict):

    #     discount = float()

    #     return discount


    