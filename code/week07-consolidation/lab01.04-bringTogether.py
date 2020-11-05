import requests
import json
from xlwt import *

dateToSearch="2020-10-10"
#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url= "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>"+dateToSearch
print (url)
response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]
#print (totalPages)
listOfReports = []

pageNumber=1
while pageNumber <= totalPages:
    pageUrl = url + "&page="+ str(pageNumber)
    #print (pageUrl)
    data = requests.get(pageUrl).json()
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])

    pageNumber +=1





w = Workbook()
ws = w.add_sheet('cars')
rowNumber = 0;
ws.write(rowNumber,0,"StartTime")
ws.write(rowNumber,1,"EndTime")
ws.write(rowNumber,2,"ImbalanceVolume")
ws.write(rowNumber,3,"ImbalancePrice")
ws.write(rowNumber,4,"ImbalanceCost")
rowNumber += 1 

for ReportName in listOfReports:
    #print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    #print(url)
    response= requests.get(url)
    #print (response.json())
    aReport= response.json()
    try:
        #I probably should use aReport.get(rows) then we check for a TypeError
        # I just like seeing that the reports are not fomatting the way I thought they should be
        #for row in aReport.get('rows'):
        for row in aReport["rows"]:

            #print (row)
            #print(row["ImbalancePrice"])
            ws.write(rowNumber,0,row["StartTime"])
            ws.write(rowNumber,1,row["EndTime"])
            if "ImbalanceVolume" in row:
                ws.write(rowNumber,2,row["ImbalanceVolume"])
            if "ImbalancePrice" in row:
                ws.write(rowNumber,3,row["ImbalancePrice"])
            if "ImbalanceCost" in row:
                ws.write(rowNumber,4,row["ImbalanceCost"])
            rowNumber += 1
    except KeyError:
        print ("the report at " + url +" does not have a attribure called row" )
w.save('balance.xls')    





