import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# The code for importing the .csv file works
os.chdir("D:/dong/Practical7")
covid_data = pd.read_csv('full_data.csv') 
covid_data.info()
#the second column from every 100th row from the first 1000 rows
print(covid_data.iloc[0:1001:100,1])
# use a Boolean to show 'total_cases for all rows corresponding to Afghanistan
afg = []
for i in covid_data.loc[:,'location']:
        afg.append(i == 'Afghanistan')
print('Boolean:', covid_data.loc[afg,'total_cases'])
# the mean numbers of new cases and new deaths on 31 March 2020
date3_31 = []
for i in covid_data.loc[:,'date']:
    date3_31.append(i == '2020-03-21')
new_date = covid_data.loc[date3_31,'date']
nc331 = covid_data.loc[date3_31,'new_cases']
nd331 = covid_data.loc[date3_31,'new_deaths']
nc_mean = np.mean(nc331)
nd_mean = np.mean(nd331)
print('mean of new cases:',nc_mean,'mean of new deaths:',nd_mean)
# create boxplot of new cases and new deaths on 31 March 2020
plt.boxplot([nc331,nd331])
plt.xticks(ticks=[1,2], labels=['New Cases','New Deaths'])
plt.ylabel('Number of Cases')
plt.title("New Cases and New Deaths on 31 March 2020")
plt.show()

# answer to the question
world_dates = covid_data.loc[:,'date']
world_new_cases = covid_data.loc[:,'new_cases']
world_new_deaths = covid_data.loc[:,'new_deaths']
plt.figure(figsize=(10,8))
plt.plot(world_dates, world_new_cases, 'b-',label='New Cases')
plt.plot(world_dates, world_new_deaths, 'r-',label='New Deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Number of New cases/New deaths')
plt.title('New Cases and New Deaths Worldwide over Time')
plt.xticks(fontsize = 7)
plt.legend()
plt.show()


# answer to the question
Brazil = []
for i in covid_data.loc[:,'location']:
    Brazil.append(i == 'Brazil')
bra_dates = covid_data.loc[Brazil,'date']
bra_new_cases = covid_data.loc[Brazil,'new_cases']
bra_total_cases = covid_data.loc[Brazil,'total_cases']

plt.plot(bra_dates,bra_new_cases,'b-',label='New Cases')
plt.plot(bra_dates, bra_total_cases, 'r-',label='Total Cases')
plt.xticks(bra_dates.iloc[0:len(bra_dates):3],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Number of New cases/Total cases')
plt.title('New Cases and Total Cases Developed over time in Brazil')
plt.xticks(fontsize = 7)
plt.legend()
plt.show()
