import scrapy
from scrapy.selector import Selector
from competition.items import CompetitionItem
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re
import time
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from pyvirtualdisplay import Display
from pyvirtualdisplay import Display


class MySpider(scrapy.Spider):
    name = "PublicStorage"


    allowed_domains = ['https://www.publicstorage.com']
    start_urls = ['https://www.publicstorage.com/missouri/self-storage-st-louis-mo/63129-self-storage/1038?lat=38.50227&lng=-90.33549&location=63129']
    def parse(self, response):
	display = Display(visible=0, size=(800, 600))
        display.start()

        url='https://www.publicstorage.com/missouri/self-storage-st-louis-mo/63129-self-storage/1038?lat=38.50227&lng=-90.33549&location=63129'
                #binary = FirefoxBinary('/usr/bin/firefox')
	#	driver=webdriver.Firefox(executable_path="~/Desktop/CompetitionScraper-master/geckodriver.exe",log_path=None)
	#	driver = webdriver.Firefox(firefox_binary=binary)
        driver = webdriver.Firefox()
        driver.get(url)

		#url2='http://www.a1lockerrental.com/self-storage/mo/st-louis/4427-meramec-bottom-rd-facility/unit-sizes-prices#/units?category=all'
		#driver2 = webdriver.Firefox()
                #driver2.get(url2)
                #html2 = driver.page_source
                #soup2 = BeautifulSoup(html2, 'html.parser')
                #soup.append(soup2)
                #print soup
        items = []
        inside = "Indoor"
        outside = "Outdoor"
        inside_units = ["5 x 5", "5 x 10"]
        outside_units = ["8' x 10'", "10' x 15'","5' x 6'","5' x 5'", "10' x 24", "10' x 30'", "5' x 10'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 10'", "10' x 15'", "10' x 8'",]

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(3)
        sizeTagz = soup.findAll('div',{"class":"srp_label srp_font_14"})


        rateTagz = soup.findAll('div',{"class":"srp_label alt-price"})
        #specialTagz2 = soup.select(".srp_label")
        specialTagz2 = soup.findAll('div',{"class":"srp_res_clm srp_clm90"})
        #specialTag = specialTagz2.findAll('div',{"class":"srp_v-space_$
        x = []
        for foo in specialTagz2:
                if foo.find('div',{"class":"srp_label"}):
                        bar = foo.find('div',{"class":"srp_label"}).text
                        if "$1" in bar or "Free" in bar or "50%" in bar:
                                x.append(bar)
        #		specialTagz = soup.findAll('div',{"class":"srp_v-space_10"})
        typesTagz = soup.findAll('ul',{"class":"srp_list"},)

        yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "Public Storage"
                       }
        size = []
        for n in range(len(sizeTagz)):
            #print len(sizeTagz)
#print len(specialTag)
            #print (specialTag[n]).get_text()
            #print (rateTagz[n]).get_text()
            special = re.sub(r"(?<=[a-z])\r?\n"," ",(x[n]))
            #if "Online" in special:
             #       special = "None"

            if "Outside" in (typesTagz[n]).get_text():
                if (sizeTagz[n]).get_text() in outside_units:
                    if (sizeTagz[n]).get_text() not in size:
			size.append((sizeTagz[n]).get_text())
			#print "logic hit"
			yield{
                        "special": "incomplete",
                        "rate": (rateTagz[n]).get_text(),
                        'size': ((sizeTagz[n]).get_text()),
                        "types": "Outside"

	                    }
                driver.close()

