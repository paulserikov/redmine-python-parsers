# Redmine PLugins List
# script get list of addon's names described in redmine.org and put it into text file

import time
import urllib
from BeautifulSoup import BeautifulSoup

ce = 0
cs = 0

start_time = time.time()

f = open('redmine_plugins_list.txt', 'w')

page1 = urllib.urlopen("http://www.redmine.org/plugins?page=1")
soup = BeautifulSoup(page1.read(), fromEncoding="utf-8")
hrefs = soup.find('p', attrs={'class': 'pagination'}).findAll('a', attrs={'class': 'page'})
max_range = hrefs[2].string
print max_range+" page founded"

for i in range (1,int(max_range)):
	page2 = urllib.urlopen("http://www.redmine.org/plugins?page="+str(i))
	soup = BeautifulSoup(page2.read(), fromEncoding="utf-8")
	print "Page "+str(i)

	if soup.find('table', attrs={'class': 'plugins'}):
		for item in soup.findAll('a', attrs={'class': 'plugin'}):
			print item.string
			f.write(str(item.string)+'\n')
		
	else:
		print "Some error. Possible, DOM of HTML was changed"

Total = time.time() - start_time, "seconds"
print Total

f.write('\n\n'+str(Total)+'\n')
f.close()

print Total
