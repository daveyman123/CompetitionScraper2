#!/usr/bin/python
import subprocess
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import datetime
import time
import os
from competition.spiders.AStorageInnLemay import AStorageInnLemay
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings



def sendmail(email):




    spider = AStorageInnLemay()
    crawler = CrawlerProcess(get_project_settings())

    crawler.crawl(spider)
    crawler.start()
    log.start()
    reactor.run() # the script will block here


    filez = "blah.csv" #%(datetime.datetime.now().strftime("%H"))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filez, "rb").read())


    msg = MIMEMultipart()
    msg['From'] = "djgraff1@cougars.ccis.edu"
    msg['To'] = email #"astoraginnlemay@gmail.com"
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = "Competition Report"
    msg.attach(MIMEText("Lemay"))




    content = 'example email stuff here'

    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo()

    mail.starttls()

    mail.login('djgraff1@cougars.ccis.edu','2ZNf+Uy}')

    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="data on Lemay %s.csv"'%(datetime.datetime.now().strftime("%s-%m-%d-%y")))
    msg.attach(part)


    try:

        mail.sendmail('djgraff1@cougars.ccis.edu',email,msg.as_string())
        print 'email sentasfd'
    except:
        print 'email not sent'
    os.remove(filez)

def sleep():
    time.sleep(4000)


def monitor(email):

    while True:
	weekday = datetime.datetime.today().weekday()
        curr_time = datetime.datetime.now().time()
        curr_hour = curr_time.hour
	print curr_hour
	time.sleep(3)
       # if weekday == 1 or weekday == 2 or weekday == 4:
	##	if curr_hour == 12:
	sendmail(email)
	break;
#	sleep()
def main(email):


    monitor(email)

if __name__ == "__main__":
    main(email)

