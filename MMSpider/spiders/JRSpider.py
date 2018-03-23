# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from MMSpider.items import MM176TypeItem,MM176PersonItem
from scrapy.loader import ItemLoader
import re
from scrapy_redis.spiders import RedisCrawlSpider,RedisSpider


class JrspiderSpider(RedisCrawlSpider):
    name = 'JRSpider'
    allowed_domains = ['www.17786.com']
    # start_urls = ['http://www.17786.com/juru.html']
    redis_key = "jspider:starts_url"
    download_delay = 1

    rules = (
        Rule(LinkExtractor(allow=(r".*(\d+_\d{1,2})",), restrict_css="div.falls-detail div.fanxiang"),callback="get_oneCollect", follow=True),
        Rule(LinkExtractor(allow=(r".*(\d+_\d{1,2})",),restrict_css=("div#container",),restrict_xpaths=("//div[@class='wt-pagelist']//span[@class='cur-page']/following-sibling::a[1]",)),callback="get_oneCollect",follow=True)
    )

    def parse_start_url(self, response):
        As = response.css("div.falls-detail div.falls-nav div:nth-of-type(4) a")
        for oneType in As:
            name = oneType.css("a::text").extract_first()
            url = oneType.css("a::attr(href)").extract_first()
            item = MM176TypeItem()
            item["name"] = name
            item["url"] = url
            yield item

    def get_oneCollect(self,response):
        #得到某个人物下面Responsehttp://www.17786.com/8501_1.html
        print(response.url)
        idGroup = re.match(r".*\.com\/(\d+)_\d+.html",response.url)
        last = False
        if idGroup:
            id = idGroup.group(1)
            loader = ItemLoader(MM176PersonItem(),response=response)
            loader.add_value("id",id)
            loader.add_css("title",".falls-detail .pageheader h2::text")
            loader.add_xpath("href","//div[@class='falls-detail']//img[@class='IMG_show']/@src")
            loader.add_css("tags",".tags_search ul li a::text")
            # loader.add_xpath("last","//div[@class='wt-pagelist']//span[@class='cur-page']/following-sibling::a[1]")
            loader.add_xpath("next", "//div[@class='content']//div[@class='img_box']/a/@href")
            item = loader.load_item()
            yield item

