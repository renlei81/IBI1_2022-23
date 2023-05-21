import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# The code for importing the .csv file works
os.chdir("D:/dong/Practical7")
covid_data = pd.read_csv('full_data.csv') 
covid_data.info()
#the second column from every 100th row from the first 1000 rows
covid_data.iloc[0:999:100,1]
# use a Boolean to show 'total_cases for all rows corresponding to Afghanistan
afg = []
for i in covid_data.loc[:,'location']:
        afg.append(i == 'Afghanistan')
print(covid_data.loc[afg,'total_cases'])
# the mean numbers of new cases and new deaths on 31 March 2020
date3_31 = []
for i in covid_data.loc[:,'date']:
    date3_31.append(i == '2020-03-21')
new_date = covid_data.loc[date3_31,'date']
nc331 = covid_data.loc[date3_31,'new_cases']
nd331 = covid_data.loc[date3_31,'new_deaths']
plt.boxplot(nc331)
plt.show()
#create boxplot of new cases adn new seaths on 31 March 2020
plt.boxplot(nd331)
plt.show()
# plot both new cases and new deaths worldwide over time
world_dates = covid_data.loc[:,'date']
world_new_cases = covid_data.loc[:,'new_cases']
world_new_deaths = covid_data.loc[:,'new_deaths']
plt.plot(world_dates, world_new_cases,'bo',world_dates,world_new_deaths,'ro',label = 'new_cases and new_deaths worldwide')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()

# answer to the question
Brazil = []
for i in covid_data.loc[:,'location']:
    Brazil.append(i == 'Brazil')
bra_dates = covid_data.loc[Brazil,'date']
bra_new_cases = covid_data.loc[Brazil,'new_cases']
bra_total_cases = covid_data.loc[Brazil,'total_cases']
plt.plot(bra_dates,bra_total_cases,'bo',bra_dates,bra_new_cases,'ro')
plt.show()
