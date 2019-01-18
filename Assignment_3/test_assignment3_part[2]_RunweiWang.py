###2
####a
import pandas as pd
import random
date_2018 = pd.date_range('2018-1-1','2018-12-31')
#using panda.datetime 
value = [random.randint(0,100) for i in range(365)]
year = date_2018.year
month = date_2018.month
day = date_2018.day
weekday = date_2018.dayofweek
a = {"Year": year,
     "Month": month,
     "Day": day,
     "Weekday": weekday,
     "Value": value}
dailyValues1 = pd.DataFrame(a)
dailyValues1.Month = dailyValues1.Month.replace([1,2,3,4,5,6,7,8,9,10,11,12],["January","February","March","April","May","June","July","August","Septemer","October","November","December"])
dailyValues1.Weekday = dailyValues1.Weekday.replace([0,1,2,3,4,5,6],["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])




####b
dailyValues2 = dailyValues1.pivot(index = "Month", columns = "Day", values = "Value")
#Return reshaped DataFrame organized by given index / column values
dailyValues2 = dailyValues2.reindex(["January","February","March","April","May","June","July","August","Septemer","October","November","December"])
#Change the order
