import requests
import json


# remove the minus sign
apiKey = '1ad149b82e90e57cb1fce60d0ea587192bcd11de'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

