
import scrapy
from scrapy.selector import Selector
from business.items import TesttestItem
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re
import time
#from pyvirtualdisplay import Display


class MySpider(scrapy.Spider):
	name = "AStorageInnLemay"

	allowed_domains = ['http://www.python.org']
	start_urls = ['http://www.python.org']

	def parse(self, response):
#                display = Display(visible=0, size=(800, 600))
 #               display.start()
		#url = "http://www.python.org"
                url='https://www.storageinns.net/self-storage/mo/saint-louis/lemay-ferry-road/#/units?category=all'
                driver = webdriver.Firefox()
		time.sleep(10)
                driver.get(url)
		time.sleep(10)
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
		outside_units = ["10 x 15","5 x 15", "8 x 10","10 x 10","10 x 20","10 x 25","10 x 30","10 x 24"]
		driver.execute_script("window.scrollTo(0, 111);")
		#print soup.findAll('span',{"class":"sss-unit-size"})
		time.sleep(4)
                SCROLL_PAUSE_TIME = 0.5
                driver.execute_script("window.scrollTo(0, 444);")
                # Get scroll height
                time.sleep(5)
                #last_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script("window.scrollTo(0, 1111);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 2222);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 3333);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 4444);")
                time.sleep(2)
		driver.execute_script("window.scrollTo(0, 2222);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 3333);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 4444);")
                time.sleep(2)

                driver.execute_script("window.scrollTo(0, 5555);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 6666);")
                time.sleep(2)
                driver.execute_script("window.scrollTo(0, 7777);")
                time.sleep(2)
               # while True:
                #     Scroll down to bottom
                driver.execute_script("window.scrollTo(0, 9999);")
                time.sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                sizeTagz = soup.findAll('span',{"class":"sss-unit-size"})
		#sizeTagz2 = soup2.findAll('span',{"class":"sss-unit-size"})

                    # Wait to load page
                    #time.sleep(SCROLL_PAUSE_TIME)
                    #print "loooping"
                    # Calculate new scroll height and compare with last scroll height
                    #new_height = driver.execute_script("return document.body.scrollHeight")
                    #if new_height == last_height:
                     #   break
                    #print "loooping"
                    #last_height = new_height
                    #print "loooping"
		
		rateTagz = soup.findAll('p',{"class":"price unit-price"})
		

		specialTagz = soup.findAll('span',{"class":"unit-special-offer"})
		typesTagz = soup.findAll('div',{"class":"unit-info"},)
		
		#rateTagz2 = soup2.findAll('p',{"class":"unit-special-offer"})
		

		#specialTagz2 = soup2.findAll('span',{"class":"unit-special-offer"})
		#typesTagz2 = soup2.findAll('div',{"class":"unit-info"},)
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "AStorageInnLemay"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        print len(rateTagz)
                        print len(typesTagz)
                        
                        if "Outside" in (typesTagz[n]).get_text():
                                if (sizeTagz[n]).get_text() in outside_units:
                                	if (sizeTagz[n]).get_text() not in size:
                                
                                                size.append((sizeTagz[n]).get_text())
                                
                                
                                #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                  	                        print "logic hit"
                
                        	                yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                
                        "special": (specialTagz[n]).get_text(),
                        "rate": re.findall('\d+\.\d+',(rateTagz[n]).get_text()),
                        'size': ((sizeTagz[n]).get_text()),
                        "types": "Outside"
	
		}
                driver.close()
                
