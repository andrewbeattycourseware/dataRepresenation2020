import requests
import json
from xlwt import *

url = "https://ie.openfoodfacts.org/brands.json"
response =  requests.get(url)

#print (response.json())

tags = response.json().get('tags')

#print  (tags)

w = Workbook()
ws = w.add_sheet('brands')
rowNumber = 0
ws.write(rowNumber, 0, "name")
ws.write(rowNumber, 1, "number of products")
ws.write(rowNumber, 2, "URL")

rowNumber += 1

for tag in tags:
    try:
        ws.write(rowNumber, 0, tag["name"])
        ws.write(rowNumber, 1, tag["products"])
        if "url" in tag:
            ws.write(rowNumber, 2, tag["url"])    
        rowNumber += 1
    except KeyError:
        print("error with row "+tag)
w.save('brands.xls')

print("all done")







