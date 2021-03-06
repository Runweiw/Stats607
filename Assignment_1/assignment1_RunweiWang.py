# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:12:17 2018

@author: Runwei
"""
#1.2
def equal_length(lst):
    for i in range(0,len(lst)-1):
        if len(lst[i]) == len(lst[i+1]):
            return True
        else:
            return False
      
#1.3
def get_states(lst):
    states = [] #define an empty list without clear its length
    for i in range(0,len(lst)-1):
        states.append(lst[i][0]) #add one element at the end of states[], which is list[i][0]
    return(states)

#1.4
def equal_vc(lst):
    total_vc = []
    for i in range(0,len(lst)):
        total_vc.append(sum(lst[i][3:7])) #3:6 means 3,4,5. So here should be 3:7
        if total_vc[i] == lst[i][2]:
            return True
        else:
            return False
def equal_pc(lst):
    total_pc = []
    for i in range(0,len(lst)):
        total_pc.append(sum(lst[i][8:11]))
        if total_pc[i] == lst[i][7]:
            return True
        else:
            return False

#1.5
import copy
def equal_total(lst):
    total = copy.deepcopy(lst)
#deepcopy:copy lst
#here is a list within another list, so simply copy can't achieve our goal
    for i in range(1,len(total[1])): 
        for j in range(0,len(total)-2):
#here count the column first, and loop lines after column to get the sum of columns
            total[j+1][i] = total[j][i]+total[j+1][i] 
        if total[-1][i] == lst[-1][i]:  
            return True
        else:
            return False

#1.6
def get_crime_rate(lst):
    rate = copy.deepcopy(lst)
    for i in range(0,len(rate)): 
        for j in range(2,len(rate[1])):
            rate[i][j] = round(rate[i][j]/rate[i][1]*100000,1)
    return(rate)

#1.7
import random
def equal_rates(lst1,lst2,n):
    lst = random.sample(range(len(lst1[1])),n)
    for i in range(n):
        if lst1[lst[i]]==lst2[lst[i]]:
            print ('crimeRate:',lst1[lst[i]],'\n', 'crimeOriginalRates:',
                    lst2[lst[i]], '\n', True)
        else:
            print ('crimeRate:',lst1[lst[i]], '\n', 'crimeOriginalRates:',
                    lst2[lst[i]], '\n', False)

#1.8
import operator
def top5_violent_states(lst):
    top5 = copy.deepcopy(lst)
    top5.sort(key=operator.itemgetter(2), reverse=True)
    dic = {}
    for i in range(0,5):
       dic[top5[i][0]] = top5[i][2]
    return(dic)

#1.9
def top_crime_states(lst,n,k):
    dic1 = {}
    if k>=2 and k<=10:
        lst.sort(key=operator.itemgetter(k), reverse=True)
        for i in range(0,n):
            dic1[lst[i][0]] = lst[i][2]
        return(dic1)
    else:
        return ('Warning!')
    
#1.10
import statistics
def crime_stats(lst,k):
    total = [None]*(len(lst)-1) #def a new list called total, and its length is [None]*(len(lst)-1)
    for i in range(0,len(lst)-1): 
        total[i]=lst[i][k]
    mean = statistics.mean(total)
    std = statistics.stdev(total)
    var = statistics.variance(total)
    return('The mean, standard deviation, and variance of are:',
           mean, std, var)
    