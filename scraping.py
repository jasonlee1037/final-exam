# anchor extraction from html document
from bs4 import BeautifulSoup
import urllib2
 
webpage = urllib2.urlopen('http://dailybruin.com/category/news/')
soup = BeautifulSoup(webpage)

#for anchor in soup.find_all("div", class_="medium"):
#find all h2 tags
for articleH2 in soup.find_all('h2'):
	#find all a tags in h2
	#title = False excludes those annoying headers
	for anchorA in articleH2.find_all('a', title = False):
		#print just the strings
		ancStr = anchorA.string

		#make the link - DB only gives the path after .com
		articleLink = "http://dailybruin.com" + (anchorA.get('href'))
		#open the link
		webpageA = urllib2.urlopen(articleLink)
		soupA = BeautifulSoup(webpageA)
		pCount = 0
		#only the paragraphs that are for the article!
		for div in soupA.find_all("div", class_= "db-post-content"):
			for p in div.find_all("p"):
				pCount +=1
		print ancStr + ": " + str(pCount) + " paragraphs"


