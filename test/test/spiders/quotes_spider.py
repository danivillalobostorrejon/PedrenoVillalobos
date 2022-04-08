
# -*- coding: utf-8 -*-
import scrapy
from test.items import QuotelItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item=QuotelItem()
            item["text"] = quote.css('.text::text').extract_first()
            item["author"] = quote.css('.author::text').extract_first()
            item["tags"] = quote.css('.tags .tag::text').extract()
            yield item
        next = response.css('.pager .next a::attr("href")').extract_first()     #Extraiga el enlace a la página siguiente
        url = response.urljoin(next)    #Combine el enlace de la página siguiente con la URL principal en un enlace completo
        yield scrapy.Request(url=url, callback=self.parse)

