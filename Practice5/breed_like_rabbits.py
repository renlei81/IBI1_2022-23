n = 2
g = 1
while n <= 100:
    g += 1
    n = 2 ** (g+1)
print(g)

# pseudocode: repeat n * 2 and g += 1 until n > 100, print(g)
                 
