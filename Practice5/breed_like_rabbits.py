n = 2
g = 1
while n <= 100:
    n = 2 ** (g+1) # n means the number of the total rabbits
    g += 1 # g refers to the generation
print(g)

# pseudocode: repeat n * 2 and g += 1 until n > 100, print(g)
                 
