import requests
from bs4 import BeautifulSoup
import urllib2
import csv

page = "https://www.zaubacorp.com/company-list/p-1-company.html"

webpage = urllib2.urlopen(page)
soup = BeautifulSoup(webpage)

for link in soup.find_all("a", {"rel":"nofollow"}):
    webpage = urllib2.urlopen(str(link.get('href')))
    soup = BeautifulSoup(webpage)

#The list of all rows
    rows = soup.findAll('tr')
#Write to CSV
    file = csv.writer(open('...', 'a'))
    file.writerow(['CIN', 'Company', 'RoC', 'Status'])

    for row in rows:
        tds = row.find_all('td')
        try:
            CIN = str(tds[0].get_text())
            Company = str(tds[1].get_text())
            Place = str(tds[2].get_text())
            Status = str(tds[3].get_text())
            print 'CIN\t', CIN
            print 'Company\t', Company
            print 'RoC\t', Place
            print 'Status\t', Status 
        except:
            print "bad string"
            continue
        file.writerow([CIN, Company, Place, Status])


              
        

