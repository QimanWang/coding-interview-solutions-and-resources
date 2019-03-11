'''
given a amount, figure out how many coin needed to make coin,

assumption: is ary sorted, unique?
find the first demon that n can divide into.
repeat for the remainder.

'''

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	left = n
	idx = len(denoms) - 1
	coins = 0
	while left != 0:
		while left > denoms[idx]:
			idx-=1
		# found loqest denom
		coins += left//denoms[idx]
		left = left%denoms[idx]
	
	return coins
		