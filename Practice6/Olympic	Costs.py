#import numpy and matplotlib
#create a dict and add values and keys 
#use zip function to combine dorresponding keys and values as a tuple
#use sorted fuction to sort the values and print it
#use matplotlib to create a bar chart with determined ind width
#add y label xtick,ytick,
#show the bar chart

import matplotlib.pyplot as plt
import numpy as np

game_costs= {1:'Los_Angeles_1984',
            8:'Seoul_1988',
            15:'Barcelona_1992',
            7:'Atlanta_1996',
            5:'Sydney_2000',
            14:'Athens_2004',
            43:'Beijing_2008',
            40:'London_2012'}
costs = game_costs.keys()
games = game_costs.values()
print(sorted(zip(costs,games)))#sort the zipped costs and games
sc = sorted(costs) 

N = 8
ind = np.arange(N)
width = 0.34
colors = ['blue','green','red']
plt.bar(ind,sc,width,color = colors)
plt.ylabel('costs') #add y label

plt.title('Olympic_games\' costs')
sorted_game = []
for i in sc:
    sorted_game.append(game_costs[i])#sort the games
plt.xticks(ind,sorted_game)

plt.yticks(np.arange(0,45,5))
plt.show()
