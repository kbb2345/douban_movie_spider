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
    	Rule(LinkExtractor(allow='movie\.douban\.com/subject/\d{8}/',
            deny=('questions',('\d{8}/\w+'))),
    		callback='parse_movie_item',follow=True),
    	)
    def parse_movie_item(self, response):
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//h1/span[1]/text()').extract_first()
        item['summary'] = response.xpath('//div[@class="related-info"]//span[@property]/text()').extract_first()
        item['score'] = response.xpath('//div[contains(@class,"rating_self")]/strong[contains(@class,"rating_num")]/text()').extract_first()
        yield item

    def parse_start_url(self, response):
        yield self.parse_movie_item(response)
