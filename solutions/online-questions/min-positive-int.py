def solution(A):
    # write your code in Python 3.6
    set_nums = set([])
    for num in A:
        set_nums.add(num)

    i=1
    while i < 1e7:
        if i in set_nums:
            i=i+1
        else:
            return i

print(solution([1,2,3,4]))