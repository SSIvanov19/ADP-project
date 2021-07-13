import scrapy
from adpProject.items import FandomItem

class FandomSpider(scrapy.Spider):
    name = 'fandom'
    allowed_domains = ['dota2.fandom.com']
    start_urls = ['https://dota2.fandom.com/wiki/Professional_teams']

    def parse(self, response):
        ourList = [] #komunizam
        item = FandomItem()
        for href in response.css("div.teambox-name > a::attr(href)").extract():
            ourList.append(href)
        
        print()
        print()
        print('Tuka gledaj')
        print(ourList)
        print()
        print()
        
