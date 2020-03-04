'''
in :[1,2,3]
out:[1,2,3] [1,3,2]
    [2,1,3] [2,3,1]
    [3,1,2] [3,2,1]
'''


def getPermutations(array):
    # Write your code here.
    pass


'''
helper_method(arr, perm,perms):
    if arr isEmpty:
        perms.append(perm)
    else:
        for num in arr:
            newArr = remove NumFrom(arr)
            newPerm = perm+num
            helper(newArr,newPerm,perms)


[1,2,3]
let's put a pointer at 1st num,

once we reach last, we get a oernmutation









'''


def permute(nums):

    res = []

    if len(nums) <1:
        return res
    # i to keep track of how many times
    for i in range(len(nums)):
        # idx to keep track of which pos we want to move to
        for idx in range(len(nums)):

            if idx + 1 < len(nums):
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
                res.append(nums)
    return res

    # now we move the list up

ls = [1,2,3]
res = permute(ls)
print(ls)

q = []
ls = [1,2,3]
for i in range(4):
    q.append(ls)

print(q)