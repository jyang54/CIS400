#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:25:04 2021

@author: phabby
"""

import json
import csv
from collections import Counter

#Getting total data
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

#-------------------------Finally got 69682 tweet

with open ('testdata' +'.json','w',encoding = 'utf-8') as fp:
    json.dump(total_data,fp,ensure_ascii = False)
    

#Convert json file to csv file

with open ('testdata.json') as file:
    t_data = json.load(file)
    
print(len(t_data))


#Getting Pfizer CSV Dataset
pfizer = []
#kword = 'covid vaccine'
kword = 'pfizer'

for d in t_data:
    if 'pfizer' in d['full_text'].lower():
        pfizer.append(d)
    #elif 'Moderna' in d['full_text']:
        #moderna.append(d)
    
#print(len(moderna)) ---9060
keys = t_data[0].keys()

csv_file = open("pfizer_data.csv","w")
dict_writer = csv.DictWriter(csv_file, keys)
dict_writer.writeheader()
dict_writer.writerows(pfizer)
csv_file.close()


#Getting Moderna CSV Dataset
moderna = []
#kword = 'covid vaccine'
kword = 'moderna'
#kword2 = 'Moderna'
for d in t_data:
    if 'moderna' in d['full_text'].lower():
        moderna.append(d)
    #elif 'Moderna' in d['full_text']:
        #moderna.append(d)
    
#print(len(moderna)) ---9060
keys = t_data[0].keys()

csv_file = open("moderna_data.csv","w")
dict_writer = csv.DictWriter(csv_file, keys)
dict_writer.writeheader()
dict_writer.writerows(moderna)
csv_file.close()


#Getting J&J CSV Dataset
janssen = []
#kword = 'covid vaccine'
#kword1 = 'janssen'
kword2 = 'j&j'
for d in t_data:
    if 'janssen' in d['full_text'].lower():
        janssen.append(d)
    elif 'johnson' in d['full_text'].lower():
        janssen.append(d)
    elif 'j amp j' in d['full_text'].lower():
        janssen.append(d)
    else:
        continue
        
#print(len(janssen)) ---5783
keys = t_data[0].keys()

csv_file = open("janssen_data.csv","w")
dict_writer = csv.DictWriter(csv_file, keys)
dict_writer.writeheader()
dict_writer.writerows(janssen)
csv_file.close()

'''
longstr = ''
for i in janssen:
    longstr = longstr + i['full_text']
split_it = longstr.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(6)
print(most_occur)
for m in most_occur:
    print(m[0],m[1])
    print(type(m))
#print(type(most))
'''


##Getting Neutral csv Dataset   
neu_data = []
for d in t_data:
    if d['analysis'] == 'neutral':
        neu_data.append(d)
        
#print(len(neu_data)) --- 22669


keys = t_data[0].keys()

csv_file = open("neu_data.csv","w")
dict_writer = csv.DictWriter(csv_file, keys)
dict_writer.writeheader()
dict_writer.writerows(neu_data)
csv_file.close()


#Getting Negative csv Dataset
neg_data = []
for d in t_data:
    if d['analysis'] == 'negative':
        neg_data.append(d)
        
#print(len(neg_data)) ----10205


keys = neg_data[0].keys()

csv_file = open("neg_data.csv","w")
dict_writer = csv.DictWriter(csv_file, keys)
dict_writer.writeheader()
dict_writer.writerows(neg_data)


#Getting Positive csv Dataset
pos_data = []
for d in t_data:
    if d['analysis'] == 'positive':
        pos_data.append(d)
        
#print(len(pos_data)) ----36808


keys = pos_data[0].keys()

csv_file = open("pos_data.csv","w")
dict_writer = csv.DictWriter(csv_file, keys)
dict_writer.writeheader()
dict_writer.writerows(pos_data)
csv_file.close()







