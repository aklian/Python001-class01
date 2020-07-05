# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from myproject.items import MyprojectItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        
