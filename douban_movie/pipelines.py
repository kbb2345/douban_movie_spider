# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import redis

class DoubanMoviePipeline(object):
	def process_item(self, item, spider):
		print(item['name'],'*'*50)
		if int(item['score']) >= 8:
			print('*'*50)
			self.redis.hmset('douban_movie:items','score',items["score"],
				'url',item['url'],'summary',item['summary'],
				'name',item['name'])
		return item
	def open_spider(self,spider):
		self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)