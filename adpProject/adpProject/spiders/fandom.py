import scrapy


class FandomSpider(scrapy.Spider):
    name = 'fandom'
    allowed_domains = ['https://dota2.fandom.com/']
    start_urls = ['https://dota2.fandom.com/wiki/Professional_teams']

    def parse(self, response):
        item = 
