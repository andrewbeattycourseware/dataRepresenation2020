

import requests
import csv
from bs4 import BeautifulSoup
url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=54.7210798611;long=-8.7237392806"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')


listings = soup.findAll("time")

for listing in listings:
    #print (listing)
    fromtime = listing['from']
    print (fromtime)
    
    windspeedelem = listing.find("windSpeed")
    if windspeedelem:
        mps = windspeedelem['mps']
        print (mps)
    #gotta go

#print (soup.prettify())

