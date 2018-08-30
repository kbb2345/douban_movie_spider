# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from douban_movie.items import MovieItem

class AwesomeMovieSpider(CrawlSpider):
    name = 'awesome_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']
    rules = (
    	Rule(LinkExtractor(allow=r'movie\.douban\.com/.*?',),
    		callback='parse_movie_item',follow=True),
    	)
    def parse_movie_item(self, response):
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//h1/span[1]/text()').extract_first()
        item['summary'] = response.xpath('//div[@id="link-report"]/span/span/text()').extract_first().strip()
        item['score'] = response.xpath('//div[contains(@class,"rating_self")]/strong[contains(@class,"rating_num")]/text()').extract_first()
        yield item

    def parse_start_url(self, response):
        yield self.parse_movie_item(response)


    def parse_page(self, response):
        yield self.parse_movie_item(response)