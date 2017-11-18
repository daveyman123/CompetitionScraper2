from scrapy.spiders import CSVFeedSpider
from business.items import TesttestItem

import scrapy
import csv
from scrapy.selector import Selector

import datetime
import re

class MySpider(scrapy.Spider):

        name = "AStorageInnDoug22"

        allowed_domains = ['https://www.storageinns.net']
        start_urls = ['http://www.storageinns.net/p/self_storage/sizes_prices_9710/saint-peters-mo-63376/a-storage-inn-cave-springs-9710']

        def parse(self, response):
                titles = response.css('.unit-row')
                outside_units = ["8 x 10", "10 x 15","5 x 6", "6 x 5", "6 x 12","10 x 10","10 x 20","10 x 25", "10 x 16", "10 x 12", "10 x 14"]
                inside_units = ["5' x 5'", "5' x 10'"]
                inside = "Indoor"
                outside = "Outdoor"

                yield {'date': datetime.datetime.now().strftime("%m-%d"),
                       'name': "AStorageInn Cave Springs"
                       }
                for i in titles:
                    Special = i.css(".special_size::text").extract_first()
                    #print i.css(".sitelink_classic_unit_cell unit-special special_size::text").extract_first(),
                    #item = TesttestItem()
                    #item ["special"] = i.css(".promo::text").extract_first()
                    rate = i.css(".rate::text").extract()
                    #if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and "Drive" in i.css("li:nth-child(2)::text").extract_first():
                    if i.css(".rate::text").extract() == []:
                        rate = "call for details"
			
                                #print "second logic"
                    #if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and "Drive" in i.css("li:nth-child(2)::text").extract_first():
                    if "Outside" in i.css(".amenities+ .amenities::text").extract_first() and i.css(".size_width::text").extract_first() in outside_units and "online" not in Special  :
                            #print "second logic"
                        yield {

                        'special': Special,
                        'types': "Outside",
                        'size': i.css(".size_width::text").extract_first(),
                        'rate': rate
                        }
def main():
	donald = MySpider()
	donald.run()
if __name__ == "__main__":
	main()

