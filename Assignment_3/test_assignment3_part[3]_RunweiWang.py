###3
####3.1
import pandas as pd
mydata = pd.read_csv('trips.csv',sep = ',')
mydata.dtypes
trips1 = mydata.loc[(mydata.pickup_latitude>40) & (mydata.pickup_latitude<41.5)\
                   & (mydata.pickup_longitude>-75) & (mydata.pickup_longitude<-72)\
                   & (mydata.passenger_count>0) & (mydata.passenger_count<5)\
                   & (mydata.trip_time_in_secs>1800)]
#return to rows that satisfy conditions



####3.2
sum_trips = trips1.describe()
num_trips = sum_trips.at['count','passenger_count']
#pd.dataframe.at: fast access to one single element of the dataframe
ave_passenger = sum_trips.at['mean','passenger_count']
ave_time = sum_trips.at['mean','trip_time_in_secs']
std_time = sum_trips.at['std','trip_time_in_secs']
tripStats = (num_trips, ave_passenger, ave_time, std_time)



####3.3
mydata2 = pd.read_csv('zipcodes.csv',sep = ',')
coords = mydata2.Coords.str.split(',',expand = True).rename(columns = {0:'Latitude', 1:'Longitude'})
#split Latitude and Longitude
coords = coords.astype('float64', copy = False)
coords = coords.join(mydata2.Zipcode)
#add Zipcode to pandas dataframe

trips1.pickup_latitude = trips1.pickup_latitude.round(2)
trips1.pickup_longitude = trips1.pickup_longitude.round(2)

trips2 = pd.merge(trips1, coords, how = 'left',\
                 left_on = [trips1.pickup_latitude,trips1.pickup_longitude],\
                 right_on = [coords.Latitude, coords.Longitude])
trips2 = trips2.dropna()



####3.4
trips2.pickup_datetime = pd.to_datetime(trips2.pickup_datetime)
#change it into datetime format
grouped = trips2.groupby(pd.Grouper(freq='H',key='pickup_datetime'))
#groupby time Hour!!! key value equals tp pickup_datetime
trips3 = grouped.Zipcode.value_counts()
trips3 = trips3.to_frame()
trips3.columns = ['Count']



####3.5
weather = pd.read_csv('weather.csv',sep = ',')
trips3 = trips3.reset_index()
#convert index into columns!!!
trips3['day'] = trips3.pickup_datetime.dt.day
trips3['hour'] = trips3.pickup_datetime.dt.hour
trips3['Weekday'] = trips3.pickup_datetime.dt.weekday
trips4 = pd.merge(trips3, weather, how = 'left',\
                 left_on = [trips3.day, trips3.hour],\
                 right_on = [weather.Day, weather.Hour])
trips4 = trips4.dropna()





####3.6
trips5 = trips4.drop(['key_0','key_1','pickup_datetime','day','hour'],axis=1)


####3.7
trips6 = trips5.groupby('Zipcode').sum()
condi = trips6.loc[(trips6.Count >= 2)]
zipcode = list(condi.index.values)
trips6 = trips5[trips5.Zipcode.isin(zipcode)]



####3.8
import matplotlib.pyplot as plt
trips7 = trips6.groupby('Hour')['Count'].sum()
trips7 = trips7.to_frame()
trips7['Temp'] = trips6.groupby('Hour')['Temp'].mean()
trips7['Num'] = range(24)

fig, ax1 = plt.subplots()
ax1.set_xlabel('Per Hour')
ax1.set_ylabel('Total Trips', color='tomato')
ax1.plot(trips7.Num, trips7.Count, color='tomato')
ax1.tick_params(axis='y', labelcolor='tomato')
ax2 = ax1.twinx()
#instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Average Temperature', color='navy')  
ax2.plot(trips7.Num, trips7.Temp, color='navy')
ax2.tick_params(axis='y', labelcolor='navy')
fig.tight_layout()  
plt.show()


