'''
dynamic approach:

for each val, figure out how many ways to make the coin from prev change
1,5
[0,1,1,1,1,2,2,]
init n+1 ary size
for each denom, calc ways[i] + ways[i-denom]

return ary[n]

O(n) space
O(dn) time, d = denoms/ change
'''
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	ways = [0 for amount in range(n+1)]
	ways[0] = 1
	for denom in denoms:
		for i in range(denom,n+1):
			ways[i] = ways[i] + ways[i-denom]
	return ways[n]