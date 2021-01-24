# -*- coding: utf-8 -*-
import scrapy

# Note:- cannot change names of start_urls, parse function etc


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    # keeping only initail url in allowed_domains
    allowed_domains = ['www.worldometers.info/']
    # changing http to https in start_urls
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

        yield {
            'title': title,
            'countries': countries
        }
