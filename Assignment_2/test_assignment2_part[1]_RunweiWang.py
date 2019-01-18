# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 19:50:31 2018

@author: Runwei
"""

import gzip
import re
import datetime
import assignment2_RunweiWang as a2

#1.
with gzip.open('maccdc2012_00016.txt.gz', 'rb') as f:
    original_data = [x.rstrip().decode() for x in f]
#import data
time_data = []
ip_data1 = []
ip_data2 = []
date_ip_data = []
for i in range(len(original_data)):
    try:
        match_data = m = re.match(r'(.*) IP (.*) > ([^\s]*): (.*)$', original_data[i])
        time_data.append(match_data.group(1)) 
        #get time list
        ip_data1.append(match_data.group(2))
        #get ip1 address list
        ip_data2.append(match_data.group(3))
        #get ip2 address list
    except AttributeError:
    #skip Attribute error
        pass
datetime_data = []
for i in range(len(time_data)):
    datetime_data.append(datetime.datetime.strptime(time_data[i],'%H:%M:%S.%f'))
    #nomarlize the format of time, turn it into %H:%M:%S.%f
one_minute = []
for i in range(len(datetime_data)):
    if datetime_data[i].minute != datetime_data[i-1].minute:
    #calculate positions of different minutes
        one_minute.append(i)
one_minute.append(len(original_data))
uniq_ip1 = []
uniq_ip2 = []
for i in range(len(one_minute)):
    uniq_ip1.append(set(ip_data1[one_minute[i-1]:one_minute[i]]))
    #calculate numbers of distinct IP addresses appearing within each minute in ip1
    uniq_ip2.append(set(ip_data2[one_minute[i-1]:one_minute[i]]))
     #calculate numbers of distinct IP addresses appearing within each minute in ip2
uniq_ip = []
for i in range(len(uniq_ip1)):
    uniq_ip.append(set(uniq_ip1[i]|uniq_ip2[i]))
    #union ip1 and ip2 to obtain the final number
uniq_num = []
for i in range(len(uniq_ip)):
    uniq_num.append(len(uniq_ip[i]))
print(uniq_num)



#2.
uniq_num1 = uniq_num.copy()
uniq_num1.sort()
print('The 10th percentile of numbers of distinct IP addresses appearing within each minute is',
      a2.percentile(uniq_num1,0.1))
print('The 25th percentile of numbers of distinct IP addresses appearing within each minute is',
      a2.percentile(uniq_num1,0.25))
print('The 75th percentile of numbers of distinct IP addresses appearing within each minute is',
      a2.percentile(uniq_num1,0.75))
print('The 90th percentile of numbers of distinct IP addresses appearing within each minute is',
      a2.percentile(uniq_num1,0.90))



#3.
ip_data = ip_data1.copy()
for i in range(len(ip_data2)):
    ip_data.append(ip_data2[i-1])
dic = {}
dic = {ip_data[0]:1}
for i in range(len(ip_data)):
    if ip_data[i] in dic:
        dic[ip_data[i]] += 1
    else:
        dic[ip_data[i]] = 1
    #create a dictionary to compare values of IP address, if IP address[i]
    #is in the dictionary, then values of this key plus 1,
    #else, create a new key and let it values be 1
def a(x):
    return x/155
ip_num_sum = list(dic.values())
ip_num = list(map(a,ip_num_sum))
#turn the values of dictionary into a list
print('Times that each IP address appears is', dic)
print('Means that each IP address appears is', ip_num)

    
    
#4.
ip_num1 = ip_num.copy()
ip_num1.sort()
print('The 10th percentile of mean number of distinct times that each IP address appears within a minute is',
      a2.percentile(ip_num1,0.1))
print('The 25th percentile of mean number of distinct times that each IP address appears within a minute is',
      a2.percentile(ip_num1,0.25))
print('The 75th percentile of mean number of distinct times that each IP address appears within a minute is',
      a2.percentile(ip_num1,0.75))
print('The 90th percentile of numbers of distinct IP addresses appearing within each minute is',
      a2.percentile(ip_num1,0.90))

