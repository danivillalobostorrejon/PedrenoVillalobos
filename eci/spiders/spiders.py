import scrapy
from eci.items import eciItems
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

    info_clothing_dict = scrapy.response.xpath("//*[@id='products-list']/ul/li[1]/span") # Este xpath es relativo a la posición [1] de la lista, deberíamos hacer un bucle para sacar todos los elementos.

    info_clothing_dict = scrapy.response.xpath("//*[@class='product_list-item']/span") # Este posiblemente es más exacto?

    def parse_price(self, info_clothing_dict):
        # TO-DO: extract.pop........
        
        price = info_clothing_dict["price"]["o_price"]
        # Sacar lista de precios de los diferentes elementos

        lst_price = [float(flat_price.extract().replace(',','.').strip())
                    for flat_price in price]

        return lst_price

    # def parse_discount(self, info_clothing_dict):

    #     discount = float()

    #     return discount


    