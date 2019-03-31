'''
in:"abc",
  "yabd"

options: insert, delete, substitue
out: 2 changes, ( insert y, sub c->d)

use a dynamic programming approach to build up from the substring

    " " y a d b
" " 
a
b
c             2

O(NM) space
O(NM) time

'''
def levenshteinDistance_full_matrix(str1, str2):
    # Write your code here.

    dp_matrix = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    print(dp_matrix)
    # for r in len(str2)

    # make first column to have the values 0,1,...,len(str2)
    for i in range(1, len(str2)+1):
        dp_matrix[i][0] = dp_matrix[i-1][0]+1
    print(dp_matrix)


    for r in range(1,len(str2)+1):
        for c in range(1,len(str1)+1):
            #if match , we pick r-1,c-1
            print(r,c)
            if str2[r-1] == str1[c-1]:
                dp_matrix[r][c]= dp_matrix[r-1][c-1]
            else:
                dp_matrix[r][c]= 1+(min(dp_matrix[r-1][c-1],dp_matrix[r-1][c],dp_matrix[r][c-1]))

                
    print(dp_matrix)
    # for i in range()
    return dp_matrix[len(str2)][len(str1)]




O(NM) time
O(max(N,M)) space
we see that we only need the last 2 rows of data,

def levenshteinDistance_two_row(str1, str2):

    # # pick the smaller string to be the column size
    # if len(str1) < len(str2):
    #     smaller_str = str1
    #     bigger_str = str2
    # else:
    #     smaller_str = str2
    #     bigger_str = str1
    # 6 liner above into two
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2


    # using only two rows
    odd_row = [None for x in range(len(small)+1)]
    even_row = [x for x in  range(len(small)+1)]
    # even_row[0]=1

    print(odd_row)
    print(even_row)

    # need mechanism to reuse the two row 
    for r in range(1,len(big)+1):
        
        #determine which row to use as curr
        if r%2==0:
            curr_row = even_row
            prev_row=odd_row
        else:
            curr_row=odd_row
            prev_row=even_row

        # 6 liner into 1    
        # curr_row,prev_row = even_row,odd_row if r%2==0 else odd_row,even_row
        curr_row[0]=r
        for c in range(1, len(small)+1):

            if big[r-1] == small[c-1]:
                curr_row[c] = prev_row[c-1]
            else:
                curr_row[c] = 1+min(prev_row[c],prev_row[c-1],curr_row[c-1])
        print('-'*12)
        print(prev_row)
        print(curr_row)
        
    return even_row[-1] if len(big)%2==0 else odd_row[-1]


str1='abc'
str2='yabd'
print(levenshteinDistance_two_row(str1,str2))
