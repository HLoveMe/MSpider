# Scrapy_redis 分布式爬虫

* 需要安装的python3模块
	* scrapy 及其依赖
	* scrapy_redis及其依赖
	* mysqlclient
	* fake-useragent
	
* 安装mysql数据库（这里没有进行数据库保存）
* Redis服务
* 创建SpiderBase名称的数据库 UTF-8字符集
* 导入文件夹下的SpiderBase.sql创建表

* 运行需要必要的修改
	
	```
		Settting文件中的
			#这是使用远程Redis服务器
			REDIS_URL = 'redis://user:4634264015@服务器ip:服务器port' 
			
			#这是Redis本地服务器 必须安装本地Redis
			# REDIS_HOST = 'localhost'
			# REDIS_PORT = 6379
	```
* scrapy crawl JRSpider
* push 初始爬取网址 
	
	```
		进入Redis客户端  redis-cli | 进入服务器端
		lpush jspider:starts_url http://www.17786.com/juru.html
		爬虫开启了
	```
	

