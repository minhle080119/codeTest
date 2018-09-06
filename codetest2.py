'''
Question 2: Please write a Python script that:
  1. Reads the JSON located at https://data.cityofnewyork.us/api/views
  /25th-nujf/rows.json
  2. Maps the 'name' from each field in "columns", available at 
    JSON_ROOT['meta']['view']['columns'], to each list inside 
    JSON_ROOT['data']. (e.g. the name of the first field listed in 
    "columns" is the name of the first item in each list in "data")
  3. Outputs a JSON file containing only data for the following 
    fields: ["Child's First Name", "Gender", "Ethnicity", 
    "Year of Birth", "Rank", "Count"]
  4. Filters the aforementioned data to only the years 2012-2014, 
    then groups by "Child's First Name" and "Ethnicity", 
    and finally provides the sum of "Count" for each combination.
  5. Writes the resulting data to both JSON and CSV.
'''

import json 
from urllib.request import urlopen

# question 1: read JSON
with urlopen("https://data.cityofnewyork.us/api/views/25th-nujf/rows.json") as response:
  source = response.read()

data = json.loads(source)
nameList = []
myList = []

for item in data['meta']['view']['columns']:
  nameList.append(item['name'])

# question 2: map name to columns
for item in data['data']:
  myDict = dict()
  for i, value in enumerate(item, 0):
    myDict[nameList[i]] = value
  myList.append(myDict)

for item in myList:
  del item['sid']
  del item['id']
  del item['position']
  del item['created_at']
  del item['created_meta']
  del item['updated_at']
  del item['updated_meta']
  del item['meta']

# question 3: output file with required fields
with open('myList.json', 'w') as f:
  f.write(json.dumps(myList, indent=2))

# question 4 & question 5
newList = []
for item in myList:
  if 2012 <= int(item['Year of Birth']) <= 2014:
    newList.append(item)

childList = []
ethList = []
for item in newList:
  if item["Child's First Name"] not in childList:
    childList.append(item["Child's First Name"])
  if item['Ethnicity'] not in ethList:
    ethList.append(item['Ethnicity'])

nameDict = dict()
for child in childList:
  nameDict[child] = []
  for item in newList:
    if child == item["Child's First Name"]:
      nameDict[child].append(item)

with open('nameDict.json', 'w') as f:
  f.write(json.dumps(nameDict, indent=2))
with open('nameDict.csv', 'w') as f:
  f.write(json.dumps(nameDict, indent=2))


ethDict = dict()
for eth in ethList:
  ethDict[eth] = []
  for item in newList:
    if eth == item["Ethnicity"]:
      ethDict[eth].append(item)

with open('ethnicityDict.json', 'w') as f:
  f.write(json.dumps(ethDict, indent=2))
with open('ethnicityDict.csv', 'w') as f:
  f.write(json.dumps(ethDict, indent=2))