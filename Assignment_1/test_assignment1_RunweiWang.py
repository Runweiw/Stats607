#1.1
import assignment1_Data as a1Data #import module as 'a1Data'
crime = a1Data.get_US_crime() #assign it to a local name 'crime' with() means return to a list, 
#without() means return to a function
print(crime,'\n') 

#1.2
import assignment1_RunweiWang as a2Data #import module as 'a2Data'
print('Do the lists inside the crimes list have the same number of elements?',
      a2Data.equal_length(crime),'\n') 

#1.3
print(a2Data.get_states(crime),'\n')

#1.4
print('Does the total number of violent crimes is equal to the ‘Violent crime total’ column?',
      a2Data.equal_vc(crime),'\n')
print('Does the total number of property crimes is equal to the ‘Property crime total’ column?',
      a2Data.equal_pc(crime),'\n')

#1.5
print('Does US total values correspond to the sum of reported values for all states?',
      a2Data.equal_total(crime),'\n')


#1.6
print(a2Data.get_crime_rate(crime), '\n')
crimeRate=a2Data.get_crime_rate(crime)

#1.7
crimeRatesOriginal = a1Data.get_US_crime_rates()
a2Data.equal_rates(crimeRate,crimeRatesOriginal,3)

#1.8
print('The top 5 states with the highest violent crime rate are', 
      a2Data.top5_violent_states(crimeRate), '\n')

#1.9
crimeRate=a2Data.get_crime_rate(crime)
print(a2Data.top_crime_states(crimeRate,8,6), '\n')

#1.10
crimeRate=a2Data.get_crime_rate(crime)
print(a2Data.crime_stats(crimeRate,7))