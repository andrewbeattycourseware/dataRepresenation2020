import requests
import json


# remove the minus sign
# this API key no longer works, probably because someone saved it to GitHub
# I have made a new one and posted to  learnonline
apiKey = '7aa146eafee094d3a7b1e81aa1d8fcb0eec8b91-0'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)

