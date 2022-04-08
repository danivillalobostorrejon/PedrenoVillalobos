#-*- coding: utf-8 -*-
from email.policy import default
from http.client import responses
import scrapy
from eci.items import eciItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy import linkextractors
import json
import datetime


class eciSpider(CrawlSpider):

    name = "elcorteingles"
    allowed_domains = ["elcorteingles.es"]

    start_urls = ["https://www.elcorteingles.es/moda-hombre/ropa/"]

# we need to search for: 
# parent tag -> products-list
# class products_list-item -> span data-json
    # class = product_link
    
    def parse_price(self, response):

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
            item = eciItem(date = datetime.now().strftime('%Y-%m-%d'), id_product = i[0], name = i[1],
                    brand = i[2], category = i[3], price = i[4], 
                       price_discount = i[5], discount = i[6], perc_discount = i[7])

            yield item

    #parsed = parse_price    