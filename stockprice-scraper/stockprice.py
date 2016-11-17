'''
	@author: Aditya Natarajan
	Scrapes stock information from Bloomberg and writes into index.csv
'''
# import libraries
import urllib2  
import csv 
from bs4 import BeautifulSoup  
from datetime import datetime  
# stock symbol:country 
symbol=[ 'GOOG:US' , 'MSFT:US' , 'AMZN:US' ]
page_data=[]
for s in symbol:
	page_data.append('http://www.bloomberg.com/quote/' + s)
# to store results
result = []  
for pg in page_data:  
    page = urllib2.urlopen(pg)
    soup = BeautifulSoup(page, 'html.parser')

    # Take get company name
    name_index = soup.find('h1', attrs={'class': 'name'})
    name = name_index.text.strip() 

    # get the index price
    price_index = soup.find('div', attrs={'class':'price'})
    price = price_index.text

    # get the change in value and percentage
    change_index = soup.find('div', attrs={'class':'change-container'})
    change = change_index.text

    result.append((name, price,change))

with open('index.csv', 'a') as csv_file:  
    writer = csv.writer(csv_file)
    for name, price, change in result:
        writer.writerow([name, price, change, datetime.now()])