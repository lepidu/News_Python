# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 20:12:57 2022

@author: leisly
"""

import requests 
  

def ipInfo():
    # api-endpoint 
    URL = "https://ipinfo.io/json"
      
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
    
    # extracting data in json format 
    data = r.json() 
    #print(data['loc'].split(','))
    return data['loc'].split(',')
    

def openCageData(lat, long):
    # api-endpoint 
    URL = "https://api.opencagedata.com/geocode/v1/json"
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'q': str(lat) + '+' + str(long),
              'key':'81b73effc59c427ea621bfeffa4a59d8'} 
      
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params=PARAMS) 
    
    # extracting data in json format 
    data = r.json() 
    
    #print (data.keys())
    #print(len(data['results']))
    #print(data['results'][0].keys())
    #print(data['results'][0]['components'].keys())
    print(data['results'][0]['components']['country'])
    print(data['results'][0]['components']['city_district'])
    print(data['results'][0]['annotations']['currency']['name'])
    
    
location = ipInfo()
openCageData(location[0] , location[1])


#    '53.345995+-6.258893'
#openCageData(53.345995, -6.258893)
#openCageData(53.345995, 86.253393)
#openCageData(48, 6.258893)