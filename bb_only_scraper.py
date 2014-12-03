from time import sleep

from bs4 import BeautifulSoup
from numpy import genfromtxt
import requests
import csv 
import re
import sys
stdin, stdout = sys.stdin, sys.stdout
reload(sys)
sys.stdin, sys.stdout = stdin, stdout
sys.setdefaultencoding('utf-8')
#import ucsv as csv

my_data = genfromtxt('F:/Beachbody_amazon/Ara/wishlists/bb_product_scraper.csv', delimiter=',', dtype=None)

# initialize a session
session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'}
#print headers
orig_stdout = sys.stdout
f = open("F:/Beachbody_amazon/Ara/wishlists/bb_only_data_from_scraper.csv", "w")
sys.stdout = f
for ASIN in my_data[:]:
    #print ASIN[0:10]
    url = "http://www.amazon.com/dp/" + ASIN[0:10]
    ranktemp="#29 inNot Available"
    sleep(1.8)

    response = session.get(url, headers=headers)
    #print(response.status_code)
    soup = BeautifulSoup(response.content)
    #print soup.get_text()
    #print soup
    #print url
    #print soup.find('li', class_='zg_hrsr_item').text
    # get best seller rankings
    for rank in soup.select('ul.zg_hrsr li.zg_hrsr_item'):
        #print url.strip() + 'sfsfdf'+ rank.text.strip()
        ranktemp=rank.text.strip()
        #print >>f, ''.join((url.rstrip(''), rank.text.rstrip(''))).encode('ascii', 'ignore')
        break
    print >>f, (url.strip() + ','+ ranktemp.replace("\n"," ")).encode('ascii', 'ignore')
#myfile = open("F:/Beachbody_amazon/Ara/wishlists/result.csv","wb")
#print >>f, ''.join(((url,rank.text,'----'))).encode('utf-8')

#print >>f, ','.join(((url.rstrip('\n'),rank.text.rstrip('\n'),"----"))).encode('ascii', 'ignore')
sys.stdout = orig_stdout
f.close()

#'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'