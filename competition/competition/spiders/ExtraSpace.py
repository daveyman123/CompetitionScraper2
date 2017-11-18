import scrapy
import csv
from scrapy.selector import Selector
from competition.items import CompetitionItem
from competition import settings
import datetime
import re
class MySpider(scrapy.Spider):
	name = "ExtraSpace"

	allowed_domains = ['https://www.extraspace.com']
	start_urls = ['https://www.extraspace.com/Storage/Facilities/US/Missouri/St_Louis/501786/Facility.aspx']

	def parse(self, response):
                display = Display(visible=0, size=(800, 600))
                display.start()
                titles = response.css('.u-other , .u-popular')
                outside_units = ["10 x 15","5 x 10", "10 x 8", "5 x 15", "8 x 10","10 x 10","10 x 20","10 x 25","10 x 30","10 x 24"]
                inside_units = ["5' x 5'", "5' x 10'"]
                inside = "Indoor"
                outside = "Outdoor"

                yield {'date': datetime.datetime.now().strftime("%m-%d"),
           'name': "ExtraSpace"
           }
                for i in titles:
                    item = TesttestItem()
                    item ["special"] = i.css(".promo::text").extract_first()

                if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and i.css(".strikeout+ .rate div::text").extract() != None and "Drive" in i.css("li:nth-child(2)::text").extract_first():


                    yield {

                    'special': i.css(".promo::text").extract_first(),
                    'types': i.css("li:nth-child(2)::text").extract_first(),
                    'size': i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first(),
                    'rate': i.css(".strikeout+ .rate div::text").extract()
                    }




