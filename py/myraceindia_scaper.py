# script to get Goa River Marathon data
########################333
# API My Race
# req:
# http://www.myraceindia.com/Live_API/index.php/ControlApi/RecordContest2/Year/2017/Event_Name/Skechers Performance Goa River Marathon 2017
# responsse:
# [{"Contest_Name":"10Km Run"},{"Contest_Name":"Full Marathon"},{"Contest_Name":"Half Marathon"}]
#
# req:
# http://www.myraceindia.com/Live_API/index.php/ControlApi/Recordrbibname/Bib/102/Year/2017/Event_Name/Skechers Performance Goa River Marathon 2017
# Respo
#
# req:
# http://www.myraceindia.com/Live_API/index.php/ControlApi/Recordstudnetname/Year/2017/Event_Name/Skechers%20Performance%20Goa%20River%20Marathon%202017?term=123
#####

from lxml import html
import requests
import numpy

page = requests.get('http://www.myraceindia.com/Live_API/index.php/ControlApi/Recordrbibname/Bib/102/Year/2017/Event_Name/Skechers Performance Goa River Marathon 2017')
json_string = page.content
import json

# fetch all the data
GRM_result=[]
i=100
while i<=110 :
    page = requests.get('http://www.myraceindia.com/Live_API/index.php/ControlApi/Recordrbibname/Bib/'+str(i)+'/Year/2017/Event_Name/Skechers Performance Goa River Marathon 2017')
    parsed_json = json.loads( page.content)
    GRM_result.append(parsed_json[0])
    i = i+1

# total count
len(GRM_result)

#testing
GRM_result[2]['Name']

,GRM_result[i]['Name'])


for arunner in GRM_result:
    for key in ['Contest_Name','Name','Net_Time','Gun_Time','Contest_Rank']:
        print key,arunner[key]






for letter in 'Python':     # First Example
   print 'Current Letter :', letter

print parsed_json[1]

parsed_json[0]['Name']

Recordrbibname


import
