def buy_house(salary:int,worth:int):
    if salary * 5 >= worth: #judge if the 5 times of the year salary is bigger than the worth of the house
        print('you can buy the house')
    else: # if it is not larger
        print('you are not recommended to buy thee house')
buy_house(1,5)
# result
# you can buy the house
