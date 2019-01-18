###1
import os
import gzip
import math
import statistics as stats
import assignment3_RunweiWang as fc


#################################################################################
#################################################################################
total_2000 = []
for i in os.listdir("2000"):
    with gzip.open("2000/"+i, 'rb') as f:
        #in folder "2000", find every zip file
        content = [x.rstrip().decode() for x in f]
        #store every zip file as a list, and make this list an element of another list
    total_2000.append(content)
del total_2000[40]
#line 40 is garbled


state = []
struc_num = []
year_built = []
year_reconstruc = []
struc_length = []
ave_dailytraffic = []
condi = [1,4,5,6,7,8]
#set cnditions

for i in range(len(total_2000)):
    for j in range(len(total_2000[i])):
        if (math.isnan(fc.myfloat(total_2000[i][j][18])) is False):
            if (math.isnan(fc.myfloat(total_2000[i][j][222:228])) is False):
                if (math.isnan(fc.myfloat(total_2000[i][j][199])) is False):
                    if((int(total_2000[i][j][18]) == 1) and (fc.myfloat(total_2000[i][j][222:228]) >= 6.1)\
                       and (total_2000[i][j][373] == 'Y') and int(total_2000[i][j][199]) in condi):
                        state.append(fc.myfloat(total_2000[i][j][0:3]))
                        struc_num.append(total_2000[i][j][3:18])
                        year_built.append(fc.myfloat(total_2000[i][j][156:160]))
                        year_reconstruc.append(fc.myfloat(total_2000[i][j][361:365]))
                        struc_length.append(fc.myfloat(total_2000[i][j][222:228]))
                        ave_dailytraffic.append(fc.myfloat(total_2000[i][j][369:371]))
                        
#struc_num = [x.replace(' ', '') for x in struc_num]
#delete any space

state1 = []
struc_num1 = []
year_built1 = []
year_reconstruc1 = []
struc_length1 = []
ave_dailytraffic1 = []       
      

for i in range(len(state)):
    if ((math.isnan(fc.myfloat(state[i]))) is False):
        if ((bool(struc_num[i])) is True):
        #test if a string is empty
            if ((math.isnan(fc.myfloat(year_built[i]))) is False):
                if ((math.isnan(fc.myfloat(year_reconstruc[i]))) is False):
                    if ((math.isnan(fc.myfloat(struc_length[i]))) is False):
                        if ((math.isnan(fc.myfloat(ave_dailytraffic[i]))) is False):
                            state1.append(state[i])
                            struc_num1.append(struc_num[i])
                            year_built1.append(year_built[i])
                            year_reconstruc1.append(year_reconstruc[i])
                            struc_length1.append(struc_length[i])
                            ave_dailytraffic1.append(ave_dailytraffic[i])
                                
managable_data_2000 = list(map(list,zip(state1, struc_num1, year_built1,\
                                        year_reconstruc1, struc_length1, ave_dailytraffic1)))
#############################################################################################
#############################################################################################
total_2010 = []
for i in os.listdir("2010"):
    with gzip.open("2010/"+i, 'rb') as f:
        content = [x.rstrip().decode() for x in f]
    total_2010.append(content)
del total_2010[0]


state_new = []
struc_num_new = []
year_built_new = []
year_reconstruc_new = []
struc_length_new = []
ave_dailytraffic_new = []
condi = [1,4,5,6,7,8]


for i in range(len(total_2010)):
    for j in range(len(total_2010[i])):
        if (math.isnan(fc.myfloat(total_2010[i][j][18])) is False):
            if (math.isnan(fc.myfloat(total_2010[i][j][222:228])) is False):
                if (math.isnan(fc.myfloat(total_2010[i][j][199])) is False):
                    if((int(total_2010[i][j][18]) == 1) and (fc.myfloat(total_2010[i][j][222:228]) >= 6.1)\
                       and (total_2010[i][j][373] == 'Y') and int(total_2010[i][j][199]) in condi):
                        state_new.append(fc.myfloat(total_2010[i][j][0:3]))
                        struc_num_new.append(total_2010[i][j][3:18])
                        year_built_new.append(fc.myfloat(total_2010[i][j][156:160]))
                        year_reconstruc_new.append(fc.myfloat(total_2010[i][j][361:365]))
                        struc_length_new.append(fc.myfloat(total_2010[i][j][222:228]))
                        ave_dailytraffic_new.append(fc.myfloat(total_2010[i][j][369:371]))
                        
#struc_num_new = [x.replace(' ', '') for x in struc_num_new]


state1_new = []
struc_num1_new = []
year_built1_new = []
year_reconstruc1_new = []
struc_length1_new = []
ave_dailytraffic1_new = []       
      


for i in range(len(state_new)):
    if ((math.isnan(fc.myfloat(state_new[i]))) is False):
        if ((bool(struc_num_new[i])) is True):
            if ((math.isnan(fc.myfloat(year_built_new[i]))) is False):
                if ((math.isnan(fc.myfloat(year_reconstruc_new[i]))) is False):
                    if ((math.isnan(fc.myfloat(struc_length_new[i]))) is False):
                        if ((math.isnan(fc.myfloat(ave_dailytraffic_new[i]))) is False):
                            state1_new.append(state_new[i])
                            struc_num1_new.append(struc_num_new[i])
                            year_built1_new.append(year_built_new[i])
                            year_reconstruc1_new.append(year_reconstruc_new[i])
                            struc_length1_new.append(struc_length_new[i])
                            ave_dailytraffic1_new.append(ave_dailytraffic_new[i])
                                
managable_data_2010 = list(map(list,zip(state1_new, struc_num1_new, year_built1_new,\
                                        year_reconstruc1_new, struc_length1_new, ave_dailytraffic1_new)))
########################################################################################
########################################################################################
total_2005 = []
for i in os.listdir("2005"):
    with gzip.open("2005/"+i, 'rb') as f:
        content = [x.rstrip().decode() for x in f]
    total_2005.append(content)
del total_2005[40]


state_new1 = []
struc_num_new1 = []
year_built_new1 = []
year_reconstruc_new1 = []
struc_length_new1 = []
ave_dailytraffic_new1 = []
condi = [1,4,5,6,7,8]


for i in range(len(total_2005)):
    for j in range(len(total_2005[i])):
        if (math.isnan(fc.myfloat(total_2005[i][j][18])) is False):
            if (math.isnan(fc.myfloat(total_2005[i][j][222:228])) is False):
                if (math.isnan(fc.myfloat(total_2005[i][j][199])) is False):
                    if((int(total_2005[i][j][18]) == 1) and (fc.myfloat(total_2005[i][j][222:228]) >= 6.1)\
                       and (total_2005[i][j][373] == 'Y') and int(total_2005[i][j][199]) in condi):
                        state_new1.append(fc.myfloat(total_2000[i][j][0:3]))
                        struc_num_new1.append(total_2005[i][j][3:18])
                        year_built_new1.append(fc.myfloat(total_2005[i][j][156:160]))
                        year_reconstruc_new1.append(fc.myfloat(total_2005[i][j][361:365]))
                        struc_length_new1.append(fc.myfloat(total_2005[i][j][222:228]))
                        ave_dailytraffic_new1.append(fc.myfloat(total_2005[i][j][369:371]))
                        
#struc_num_new1 = [x.replace(' ', '') for x in struc_num_new1]


state1_new1 = []
struc_num1_new1 = []
year_built1_new1 = []
year_reconstruc1_new1 = []
struc_length1_new1 = []
ave_dailytraffic1_new1 = []       
      


for i in range(len(state_new1)):
    if ((math.isnan(fc.myfloat(state_new1[i]))) is False):
        if ((bool(struc_num_new1[i])) is True):
            if ((math.isnan(fc.myfloat(year_built_new1[i]))) is False):
                if ((math.isnan(fc.myfloat(year_reconstruc_new1[i]))) is False):
                    if ((math.isnan(fc.myfloat(struc_length_new1[i]))) is False):
                        if ((math.isnan(fc.myfloat(ave_dailytraffic_new1[i]))) is False):
                            state1_new1.append(state_new1[i])
                            struc_num1_new1.append(struc_num_new1[i])
                            year_built1_new1.append(year_built_new1[i])
                            year_reconstruc1_new1.append(year_reconstruc_new1[i])
                            struc_length1_new1.append(struc_length_new1[i])
                            ave_dailytraffic1_new1.append(ave_dailytraffic_new1[i])
                                
managable_data_2005 = list(map(list,zip(state1_new1, struc_num1_new1, year_built1_new1,\
                                        year_reconstruc1_new1, struc_length1_new1, ave_dailytraffic1_new1)))
########################################################################################
########################################################################################

L = managable_data_2000 + managable_data_2005 + managable_data_2010
#L is the final managable data of threes years






####1.1
dic1 = {}
dic1 = {L[0][0]:1}
for k in range(len(L)):
    if L[k][0] in dic1:
        dic1[L[k][0]] += 1
    else:
        dic1[L[k][0]] = 1
#using dictionary to count the number of unique structure numes
stateWithMostBridges = max(dic1, key = dic1.get)
#return key with the largest value





####1.2
dic2 = {}
dic2 = {L[0][0]:L[0][4]}
for i in range(len(L)):
    if (L[i][0] in dic2):
        dic2[L[i][0]] += L[i][4]
    else:
        dic2[L[i][0]] = L[i][4]
#compute the total length of bridges in each state
avgLenBridges = {i: float(dic2[i])/dic1[i] for i in dic1}
#average length = total/count



####1.3
shortLongStates = (min(avgLenBridges, key=avgLenBridges.get), max(avgLenBridges, key=avgLenBridges.get))
#determain states with shortest or longest bridges



####1.4
period = []
for i in range(len(L)):
    if (L[i][3]-L[i][2] > 0):
        period.append(L[i])
#find bridge that were rebuilt, which is year2 - year1 > 0
a = 0
for i in range(len(period)):
    a += period[i][3]-period[i][2]
avgRebuilt = a/len(period)
#average rebuilt = total gap years/count



####1.5
dic3a = {}
for i in range(len(managable_data_2000)):
    dic3a[managable_data_2000[i][1]] = managable_data_2000[i][5]
dic3b = {}
for i in range(len(managable_data_2010)):
    dic3b[managable_data_2010[i][1]] = managable_data_2010[i][5]
two_years = list(dic3a.keys() & dic3b.keys())
#find same bridges in both years
dic3c = {}
for i in range(len(two_years)):
    dic3c[two_years[i]] = managable_data_2010[i][5]-managable_data_2000[i][5]
#match two years' data and calculate 2010-2005(which > 0 indicates increasment)
num = list(dic3c.values())
x = 0
for i in range(len(dic3c)):
    if num[i] > 0:
        x += 1
propIncTraffic = x/len(dic3c)




#####1.6
dic4 = {}
for i in range(len(managable_data_2000)):
    if (managable_data_2000[i][1] in dic3c):
        dic4[managable_data_2000[i][1]] = managable_data_2000[i][5]
dic5 = {}
bridge = list(dic4.keys())
for i in range(len(dic3c)):
    if dic4[bridge[i]] == 0:
        if dic3c[bridge[i]] == 0:
            dic5[bridge[i]] = 0
        else:
            dic5[bridge[i]] = 1
    else:
        dic5[bridge[i]] = (dic3c[bridge[i]]/dic4[bridge[i]])
change = list(dic5.values())
avgPercentChange = stats.mean(change)





