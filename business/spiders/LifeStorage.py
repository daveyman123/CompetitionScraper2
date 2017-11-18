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
	name = "LifeStorage"
	
	allowed_domains = ['https://www.lifestorage.com']
	start_urls = ['https://www.lifestorage.com/storage-units/missouri/saint-louis/63125/312-near-mehlville/?size=5x5']

        def parse(self, response):
               #display = Display(visible=0, size=(800, 600))
               # display.start()
               
                    #print newString
                def replacenth(s, sub, repl, nth):
                    find = s.find(sub)
                    # if find is not p1 we have found at least one match for the substring
                    i = find != -1
                    # loop util we find the nth or we find no match
                    while find != -1 and i != nth:
                        # find + 1 means we start at the last match start index + 1
                        find = s.find(sub, find + 1)
                        i += 1
                    # if i  is equal to nth we found nth matches so replace
                    if i == nth:
                        return s[:find]+repl+s[find + len(sub):]
                    return s
                url='https://www.lifestorage.com/storage-units/missouri/saint-louis/63125/312-near-mehlville/?size=5x5'
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
		outside_units = ["5' x 5'","5' x 10'", "10' x 5'", "15' x 10'","10' x 15'","5' x 6'", "6' x 12'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 12'", "10' x 14'", "12' x 12'",]
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                time.sleep(3)
                sizeTagz = soup.findAll('div',{"class":"storesRow"})
		
		
		rateTagz = soup.findAll('div',{"class":"priceBox"})
		
		
                #specialTagz2 = soup.findAll('div',{"class":"srp_label"})
		
		typesTagz = soup.findAll('ul',{"class":"features"},)
		#s = soup.findAll('div',{"specialsMessage"})
		#time.sleep(3)
		#s = soup.findAll('div',{"specialsMessage"})
		#print len(s)
		special = soup.findAll('div',{"class":"priceBox"})

		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "Life Storage"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        print n
			
                        specials = special[n]
                        specialz = specials.find("div", {"class": "specialsMessage"})
                        if specialz != None:
                                specialz = specialz.get_text()
                                specialz = specialz.replace("\n", "")                        	
                        x = (sizeTagz[n]).get_text()
                        
                        #x = re.sub('[*]', '', x)
                        #x = x.replace(' ', '')
                        print x
                        #print x
                        #print (rateTagz[n]).get_text()
                        
                        if "Outdoor" in (typesTagz[n]).get_text():
                                #print "Outdoor hit"
                                for sizes in outside_units:
                                        if sizes in x:
                                                
                                 #               print "right size"
                                                if x not in size and re.findall(r'^\D*(\d+)',(rateTagz[n]).get_text()) != []:
                                                        
                                                        
                                #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                                  #                      print "logic hit"
                                                        x = re.sub('[*]', '', x)
                                                        x = x.replace(',', 'x')
                                                        x = x.replace(' ', '')
                                                        x = x.replace('8', '')
                                                        x = re.findall(r'\d+', x)
                                                        x = " ".join(str(i) for i in x)
                                                        x = x.replace(' ', 'x')
                                                        if len(x) > 5:
                                                                x = replacenth(x, "x", "/", 2)
                                                        if x not in size:
                                                                size.append(x)
                                                                #print x
                                                                #print size
                                                               
                                                                 

                                                   #             gotdata = s[n]
						#		if len(gotdata) > 5:
						#			gotdata = gotdata.get_text()		
                        		         #                       gotdata = gotdata.replace('\n', ''),
						#		else:
						#			s.insert(n, "none")

                                         	                yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                        
                                                                                "special": specialz,
                                                                                "rate": re.findall(r'^\D*(\d+)',(rateTagz[n]).get_text()),
                                                                                'size': x,
                                                                                "types": "Outside"
                                                                                        }        
                                                
                                        
				#	elif sizes not in x and len(s[n]) > 5:				
                                 #    		s.insert(n,"none")
				#		print len(s)
					

					   
                driver.close()

