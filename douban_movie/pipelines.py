# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import redis

class DoubanMoviePipeline(object):
	def process_item(self, item, spider):
		print(item['url'],'*'*50)
		if float(item['score']) >= 8:
            '''
			items = json.dumps({'score':item["score"],'url':
			item['url'],'summary':item['summary'],'name':
				item['name']})
			print('*'*50)
            '''
			self.redis.lpush('douban_movie:items',json.dumps(dict(item)))
		return item
	def open_spider(self,spider):
		self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)
