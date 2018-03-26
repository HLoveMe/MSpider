# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


"""
    User_Agent
"""
from fake_useragent import UserAgent

class MmSpiderDownLoaderUserAgent(object):
    def __init__(self):
        self.ua = UserAgent()
        pass

    def process_request(self, request, spider):
        request.headers["User-Agent"] = self.ua.random
        pass

