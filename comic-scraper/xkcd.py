import urllib
import sys
import os
from bs4 import BeautifulSoup

def getXKCD(id):
    page = urllib.urlopen('http://xkcd.com/' + str(id))
    soup = BeautifulSoup(page.read(),"lxml")  
    page.close()
    div_index = soup.find('div',attrs={'id':'comic'})
    image = div_index.find('img')
    imagelink ='http:' + image['src']
    if not os.path.exists('xkcd' + '/'):
        os.makedirs('xkcd' + '/')
    extension = imagelink.split('.')[-1]
    urllib.urlretrieve(imagelink, '%s/%s.%s' % ('xkcd', id, extension))
    print('Downloaded %d ' %id)
    return id + 1

start=1;
end=1736
ignore = [404, 1331, 1350]
for i in xrange(start, end+1):      
    if i in ignore:
        continue
    getXKCD(i)