ary = [4,2,3,1,5,2,9]

for i in ary:
    print(i)

def min_moves(target):
    min_increment = prev = 0
    
    for num in target:
        if num > prev:
            min_increment += num - prev
        prev = num
    
    return min_increment

print(min_moves(ary))

print(ord('A'))