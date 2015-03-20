# anchor extraction from html document
from bs4 import BeautifulSoup
import urllib2
 
webpage = urllib2.urlopen('http://dailybruin.com/category/news/')
soup = BeautifulSoup(webpage)
#find all h2 tags
for anchor in soup.find_all('h2'):
	#find all a tages in h2
	for anchorA in anchor.find_all('a'):
		#print just the strings
		print anchorA.string


for anchor2 in soup.find_all('h2'):
	for anchor2 in anchor2.find_all('a'):
		articles = (link.get('href'))
