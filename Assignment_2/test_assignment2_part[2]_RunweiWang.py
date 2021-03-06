# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 19:50:49 2018

@author: Runwei
"""

#Problem 2
import numpy as np

#1.
x = np.loadtxt('adverseCountsFinal.txt', delimiter='\t') 
#read text file


#2.
total_since_1968 = np.sum(x[:,1:4], axis = 0)
print(np.asarray(total_since_1968))
#make a numpy array


#3.
per_year_total = np.sum(x[:,1:4], axis = 1)
print(np.asarray(per_year_total))


#4. 
serious_max = np.amax(x[:,1], axis = 0)
#find the maximum number
serious_max_year = np.argmax(x[:,1])
#return to the position of maximum number
death_max = np.amax(x[:,2], axis = 0)
death_max_year = np.argmax(x[:,2])
non_serious_max = np.amax(x[:,3], axis = 0)
non_serious_max_year = np.argmax(x[:,3])
print(np.asarray([x[serious_max_year,0], x[death_max_year,0], x[non_serious_max_year,0]]))
print('Year of', x[serious_max_year,0], 'has the highest number of reports for Serious,', 
      'which is', int(serious_max))
print('Year of', x[death_max_year,0], 'has the highest number of reports for Death,',
       'which is', int(death_max_year))
print('Year of', x[non_serious_max_year,0], 'has the highest number of reports for Non-Serious,',
       'which is', int(non_serious_max))


#5.
y = x.copy()
max_of_year = np.argmax(y, axis = 1)
#find the position of maximum
print(np.asarray(max_of_year))
print('The type of side effect has been reported the most for each year shows below:',
      max_of_year, 'where 1 stands for "Serious", 2 stands for "Death", and 3 stands for "Non-Serious".')


#6.
z = np.delete(x,0,axis=1)
sum_of_year = np.sum(z,axis=1)
sum_of_year.shape = (51,1)
#reshape the size of x, turn it into a 51*1 array
propotion = z/sum_of_year
names = np.asarray(['Serious','Death','Non-Serious'])
propotion_of_year = np.vstack([names,propotion])
print(propotion_of_year)


#7.
import matplotlib.pyplot as plt
plot = plt.subplots()
plot = plt.stackplot(x[:,0], x[:,1], x[:,2], x[:,3],labels = ['Serious','Death','Non-Serious'])
plt.legend(loc='upper left')
plt.show()