'''
so we want to remove a node from a list,
the position is nth from last,
we can't go backwards, how do we keep track of the location?
we can create a gap between two nodes with left and right.
when the right reahed the end, we know left is at the correct location.

'''
def removeKthNodeFromEnd(head, k):
    # Write your code here.

	# two pointers 
	left = head
	right = head
	for i in range(k):
		right = right.next	
		
	# if the last pointer is null, we can just safely just update the head
	if right is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	#keep moving until we reach end
	while right.next is not None:
		left = left.next
		right = right.next
	
	# now we remove the pointers.
	left.next = left.next.next 

	