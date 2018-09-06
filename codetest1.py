'''
Question 1: Please write a Python script that:
  1. Reads the JSON located at http://mysafeinfo.com/api/data?list=englishmonarchs&format=json
  2. Outputs a JSON object consisting of lists of unique 'nm', grouped by 'cty' and 'hse'
Example output:
{
  "cty1": {
    "hse1": ["name1", "name2"],
    "hse2": ["name1", "name2"]      
  },
  "cty2": {
    "hse3": ["name1", "name2"],
    "hse4": ["name1", "name2"]      
  }    
}
'''
import json 
from urllib.request import urlopen

# question 1 read JSON
with urlopen("http://mysafeinfo.com/api/data?list=englishmonarchs&format=json") as response:
  source = response.read()

data = json.loads(source)
ctyList = [] 
hseList = []
myDict = dict()

# ctyList & hseList of unique items
for item in data:
  if item['cty'] not in ctyList: ctyList.append(item['cty'])
  if item['hse'] not in hseList: hseList.append(item['hse'])

# question 2 output JSON
for cty in ctyList:
  myDict[cty] = dict()
  for hse in hseList:
    myDict[cty][hse] = []
    for item in data:
      if hse == item['hse']: myDict[cty][hse].append(item['nm'])

print(json.dumps(myDict, indent=2))


