# anchor extraction from html document
from bs4 import BeautifulSoup
import urllib2
 
webpage = urllib2.urlopen('http://dailybruin.com/category/news/')
soup = BeautifulSoup(webpage)
#find all h2 tags

for anchor in soup.find_all("article"):
	for articleH2 in anchor.find_all('h2'):
		#find all a tages in h2
		for anchorA in articleH2.find_all('a'):
			#print just the strings
			print anchorA.string
for anchorside in soup.find_all("div", class_="medium-4 columns db-section-side hide-for-small"):
	for articleH2side in anchorside.find_all('h2'):
		#find all a tages in h2
		for anchorAside in articleH2side.find_all('a'):
			#print just the strings
			print anchorAside.string


#for anchor2 in soup.find_all('h2'):
#	for link in anchor2.find_all('a'):
#		articleLink = (link.get('href'))
#		print articleLink
