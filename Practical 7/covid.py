import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import the .csv file works
os.chdir("/Users/yumenghan/IBI1_2021-22/Practical7")
covid_data=pd.read_csv("full_data.csv")

# show the first and third columns from rows 10-20 (inclusive)
print('The first and third columns from rows 10-20 (inclusive) are')
print(covid_data.iloc[9:20,[0,2]])

# use a Boolean to show “total cases” for all rows corresponding to Afghanistan
location_wanted="Afghanistan"
my_rows=[]
for i in range(0,len(covid_data)):
    location=covid_data.iloc[i,1] #read just the “location” column, but all the rows from covid_data
    selection= location==location_wanted #create a Boolean that is True when the “location” is “Afghanistan”, but false otherwise
    my_rows.append(selection)
    i=i+1
print('The "total cases" for all rows corresponding to Afghanistan are')
print(covid_data.loc[my_rows,"total_cases"]) #use that Boolean to find exactly the rows needed in the dataframe

# computed the mean number of new cases and new deaths in China
import numpy
df = numpy.genfromtxt('china_new_data.csv',delimiter=',', usecols=(1,2), skip_header=1, usemask=True)
print('The mean number of new cases and the mean number of new casesnew deaths in China are ',numpy.mean(df,axis=0))
# The means of new cases and new deaths in China are different. It means many people are cured after infection.
df_infect = numpy.genfromtxt('china_new_data.csv',delimiter=',', usecols=(1), skip_header=1, usemask=True)
df_dead = numpy.genfromtxt('china_new_data.csv',delimiter=',', usecols=(2), skip_header=1, usemask=True)
prop = numpy.mean(df_dead,axis=0)/numpy.mean(df_infect,axis=0)
print('The proportion of new cases that kill the infected person is ',prop)

# creat a boxplot of new cases and new deaths in China worldwide
china_new_data=pd.read_csv("china_new_data.csv")
new_cases=china_new_data.iloc[:,1] 
plt.boxplot(new_cases,labels=["New cases"],patch_artist = True)
plt.title("Daily new cases in China")
plt.ylabel('Amount')
plt.show()

new_deaths=china_new_data.iloc[:,2] 
plt.boxplot(new_deaths,labels=["New deaths"],patch_artist = True)
plt.title("Daily new deaths in China")
plt.ylabel('Amount')
plt.show()

# plot both new cases and new deaths in China over time
china_dates=china_new_data['date']
china_new_cases=china_new_data['new_cases']
plt.plot(china_dates,china_new_cases,'b+')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.title("Daily new cases in China")
plt.ylabel('Amount')
plt.xlabel('Dates')
plt.show()

china_new_deaths=china_new_data['new_deaths']
plt.plot(china_dates,china_new_deaths,'r+')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.title("Daily new deaths in China")
plt.ylabel('Amount')
plt.xlabel('Dates')
plt.show()

plt.plot(china_dates,china_new_cases,label='New cases')
plt.plot(china_dates,china_new_deaths,label='New deaths')
plt.legend()
plt.title("Daily new cases and new deaths in China")
plt.ylabel('Amount')
plt.xlabel('Dates')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.show()

# answer to the question stated in file question.txt
selecting_date=[]
i=0
for i in range(0,len(covid_data)):
    date=covid_data.iloc[i,0]
    selection= date=='2020-03-31'
    selecting_date.append(selection)
    i=i+1
location_total=covid_data.iloc[selecting_date,:]

selecting_wanted=[]
i=0
n=10
for i in range(0,len(location_total)):
    cases=location_total.iloc[i,4]
    selection_location= cases<=n
    selecting_wanted.append(selection_location)
    i=i+1
location=location_total.iloc[selecting_wanted,1]    
print('The places in the World where there have not yet been more than 10 total infections (as of 31 March) are')     
print(location)



