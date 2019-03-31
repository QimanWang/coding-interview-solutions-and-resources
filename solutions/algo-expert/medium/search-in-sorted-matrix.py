'''
we can traverse the matrix, like a binary tree,

start at top right:
if tgt < m[r][c]:
	col -=1
elif tgt > m[r][c]:
	row +=1
else:
	return [row,col]
'''

def searchInSortedMatrix(matrix, target):
    # Write your code here.
	
	
	r = 0
	c = len(matrix[0]) - 1

	while r < len(matrix) and c >=0:
		if target < matrix[r][c]:
			c-=1
		elif target > matrix[r][c]:
			r+=1
		else:
			return [r,c]
	
	return [-1,-1]
		