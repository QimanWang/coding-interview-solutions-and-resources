loc = [2,2]
print(loc)

increment = [0,1,0,-1,0]

for i in range(len(increment)-1):
    newr = loc[0] + increment[i]
    newc = loc[1] - increment[i+1]
    print([newr,newc])


