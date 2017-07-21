#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple spider made with Scrapy that scraps data from a list of pages.
"""

import scrapy

class BasicSpider(scrapy.Spider):
    name = 'basicspider'
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(BasicSpider, self).__init__(*args, **kwargs)
        # read input file that contains pages to crawl
        with open(kwargs.get('file')) as f :
            self.start_urls = f.read().splitlines()

    def parse(self, response):
        yield {
            "url": response.url,
            "title": response.css('title::text').extract_first(),
            "description": response.css("meta[name=description]::attr(content)").extract_first()
        }
