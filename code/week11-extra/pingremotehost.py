import mysql.connector
import requests


count=1
working=True
while (working):
    url = "http://andrewbeatty1.pythonanywhere.com/books"

    response = requests.get(url)
    statusCode = response.status_code
    print (statusCode)
    working=False