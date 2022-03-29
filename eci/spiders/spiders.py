import scrapy
from eci.items import eciItems
from scrapy.spiders import CrawlSpider, Rule
from scrapy import linkextractors


class eciSpider(CrawlSpider):

    name = "eci"
    allowed_domains = ["elcorteingles.es"]


    start_url = ["https://www.elcorteingles.es/moda-hombre/ropa/"]

# we need to search for: 
# class products_list-item -> span data-json
    # class = product_link

    