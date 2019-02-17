# sort the array 
# 3 points: curr(left most), L(right after curr) , R(last item)
# if the 3 sums to target, add the set as solution,
    # move both pointer inside, if ary vals r unique
# if less move left pointer to get a bigger num
# if greater move right to get a smaller num
# we stop when the L,R cross each other, move curr by 1
# keep repeat until curr cross l or r

# time O(n^2): 1 path for c, l+r also 1 path , tho quicksort is O(nlg(n))
# space O(N) : upperbound for the case where every val is a solution

def threeNumberSUm(array, targetSum):
    array.sort()
    triplets = []
    # i is the curr
    for i in range(len(array) - 2):
        left = i+1
        right = len(array)-1
        # prevent crossing each other
        while left < right :
            currSum = array[i] + array[left] + array[right]
            if currSum == targetSum:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif currSum < targetSum:
                left +=1
            elif currSum > targetSum:
                right -=1
    
    return triplets 

print(threeNumberSUm([1,2,3,4,5,6,7,8],10))


            






