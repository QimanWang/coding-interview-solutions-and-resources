'''
hmmm, we can grow out or backet in.
grow out would require jumping around too much.

let's try backeting it in.

start from both end of str.
then move the pointers inward if the charatcers are not the same.
maybe we can move left, maybe we can move right

bracketing is not good.
let's try to just go with the expansion method.


edge case:
-char length?
-start at 2nd char?

we check if possible palindrom
1. right match curr, even palindrom
2. left and right match, odd palindrome.

if palindrom, we keep expanging the two sides.
#

'''	
def longestPalindromicSubstring(string):

    max_pal = ""

    if len(string) < 2:
        return string

    for i in range(1,len(string)-1):
        #odd
        temp_max_pal=''
        if string[i-1]==string[i+1]:
            #expand both side
            temp_max_pal=expand(string,i-1,i+1)

        #even
        elif string[i]==string[i+1]:
            temp_max_pal=expand(string,i,i+1)

        if len(temp_max_pal) >len(max_pal):
            max_pal=temp_max_pal
        

    return max_pal


def expand(string, leftidx,rightidx):
    while leftidx >=0 and rightidx < len(string):
        if string[leftidx]!=string[rightidx]:
            break
        else :
            leftidx-=1
            rightidx+=1
        
    return string[leftidx+1:rightidx] 



# print(longestPalindromicSubstring('abaxyzzyxf'))
# s='z234a5abbba54a32z'  # 5abbba5
s='z234a5abbba54a32z'  # 5abbba5
print(longestPalindromicSubstring(s))
  
