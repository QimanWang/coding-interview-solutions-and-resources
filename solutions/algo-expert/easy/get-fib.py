'''
fib is defind as a sequence, 0,1,n-1 + n-2,
'''

def getNthFib(n):
    
    '''
    # a,b = 0,1
    # for i in range(n):
    #     print("i"+str(i))
    #     a,b = b, a+b    
    
    # return a
    '''
    if n <3:
        return 0 if n==1 else 1


    lastTwo =[0,1]
    counter =3
    while counter <=n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0]= lastTwo[1]
        lastTwo[1]= nextFib
        counter+=1

    return lastTwo[1]

for i in range(1,6):
    print(i)
    # print(getNthFib(i))
