# -*- coding: utf-8 -*-
import scrapy

#https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

class ExampleSpider(scrapy.Spider):
    name = 'gakbot'
    allowed_domains = ['gak.co.uk']
    start_urls = ['https://www.gak.co.uk/en/stratocaster']

    def parse(self, response):
        # Extracting the content using css selectors
        titles = response.css("section.productDescription > h3::text").extract()

        #this works
        price = response.css('p.price::text').extract()

        #title = response.css(".productDescription::attr('h3')").extract()[0]


        # Give the extracted content row wise
        for item in zip(titles, price):
            # create a dictionary to store the scraped info
            scraped_info = {
                'titles': item[0],
                'price': item[1]

            }

            # yield or give the scraped info to scrapy
            yield scraped_info




