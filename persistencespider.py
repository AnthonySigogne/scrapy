#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple spider made with Scrapy that scraps data from a list of pages,
and saves it in the Elasticsearch database.
"""

import scrapy
import elasticsearch

# open elasticsearch connection
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=["localhost"], http_auth=("elastic", "changeme"), port=9200)

class PersistenceSpider(scrapy.Spider):
    name = 'persistencespider'
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(PersistenceSpider, self).__init__(*args, **kwargs)
        # read input file that contains pages to crawl
        with open(kwargs.get('file')) as f :
            self.start_urls = f.read().splitlines()

    def parse(self, response):
        doc = {
            "url": response.url,
            "title": response.css('title::text').extract_first(),
            "description": response.css("meta[name=description]::attr(content)").extract_first()
        }
        res = es.index(index="web", doc_type='page', body=doc)
        print(res['created'])
        yield doc
