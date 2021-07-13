import scrapy
import logging
from adpProject.items import FandomItem

class FandomSpider(scrapy.Spider):
    name = 'fandom'
    allowed_domains = ['dota2.fandom.com']
    start_urls = ['https://dota2.fandom.com/wiki/Professional_teams']

    def extractInfo(self, response):
        item = FandomItem()
        item = {
                "name": response.xpath("""//*[@id="firstHeading"]/text()""").get(),
                "country": response.xpath("""//*[@id="mw-content-text"]/div/table[1]/tbody/tr[3]/td/a/@title""").get(),
                "imgLink": response.xpath("""//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td/a/img/@src""").get()
        }

        yield item


    def parse(self, response):
        logging.getLogger('scrapy').propagate = False
        for href in response.css("div.teambox-name > a::attr(href)").extract():
            yield scrapy.Request("https://dota2.fandom.com" + href, callback=self.extractInfo) 
