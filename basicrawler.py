#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse

class Crawler(CrawlSpider):
    name = 'basicrawler'
    start_urls = []
    allowed_domains = []
    rules = (
        # Extract all inner domain links with state "follow"
        Rule(LinkExtractor(), callback='parse_items', follow=True, process_links='links_processor'),
    )

    def __init__(self, *args, **kwargs):
        super(CrawlSpider, self).__init__(*args, **kwargs)
        # read input file that contains domains to crawl
        with open(kwargs.get('file')) as f :
            self.start_urls = f.read().splitlines()
            self.allowed_domains = [urlparse(url).netloc for url in self.start_urls]
        self._compile_rules()

    def links_processor(self,links):
        """
        A hook into the links processing from an existing page, done in order to not follow "nofollow" links
        """
        ret_links = list()
        if links:
            for link in links:
                if not link.nofollow:
                    ret_links.append(link)
        return ret_links

    def parse_items(self, response):
        yield {
            "url": response.url,
            "title": response.css('title::text').extract_first(),
            "description": response.css("meta[name=description]::attr(content)").extract_first()
        }
