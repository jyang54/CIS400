#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:25:04 2021

@author: phabby
"""

import json
import csv


total_data = []

with open ('0428-10000.json') as file:
    data0 = json.load(file)

total_data = total_data + data0

with open ('0429-10000.json') as file:
    data1 = json.load(file)

total_data = total_data + data1

with open ('0430-10000.json') as file:
    data2 = json.load(file)
    
total_data = total_data + data2
    
with open ('0501-10000.json') as file:
    data3 = json.load(file)
    
total_data = total_data + data3

with open ('0502-10000.json') as file:
    data4 = json.load(file)
    
total_data = total_data + data4
    
with open ('0503-10000.json') as file:
    data5 = json.load(file)
    
total_data = total_data + data5

with open ('0504-10000.json') as file:
    data6 = json.load(file)
    
total_data = total_data + data6

#Remove duplicate dictionaries (tweets) from the list

total_data = [dict(t) for t in set([tuple(d.items()) for d in total_data])]
#print(len(total_data))

#Finally got 69682 tweet

with open ('testdata' +'.json','w',encoding = 'utf-8') as fp:
    json.dump(total_data,fp,ensure_ascii = False)
    


#Convert json file to csv file

with open ('testdata.json') as file:
    t_data = json.load(file)

keys = t_data[0].keys()

csv_file = open("t_data.csv","w")
dict_writer = csv.DictWriter(csv_file, keys)
dict_writer.writeheader()
dict_writer.writerows(t_data)
csv_file.close()







