"""array:
O(1) retrieve
size O(1) insert
constant size, use for exact amount of elements
ex: store char count, only 26 char
"""

"""Linkedlist:
O(n) retrieve
O(1) insert
dynamic size, useful for unknown # of elements, not good for traversal
ex: store list of names
"""

"""Arraylist
O(1) retrieve
O(1) insert
best of both world from array and list
dynamically increase/decrease as needed
ex: python uses it (:
"""
ary_list = [1,2,'3']
for i in range(len(ary_list)):
    print(ary_list[i])

"""Queue
FIFO: First In First Out
O(1) retrieve from the front
O(1) insert at the end,push() is the og method,
but python list use append() at end or insert()
ex: process elements in order they're inserted
note: python has a syncronized queue class for multi threading,
otherwise we can use the built in list class, but list can run into issues
because python list store elements next to each other in memory,
which can lead to speed issue for inserting large amount of elements

collections.deque
queue.Queue queue.LifoQueue 
"""
queue = ['first']
queue.insert(len(queue),'second')
queue.insert(len(queue),'third')
queue.append('fourth')
print(queue)

print(f"popped: {queue.pop(0)}")
print(f"popped: {queue.pop(0)}")
print(f"popped: {queue.pop(0)}")
print(queue)

"""Stack
LILO: Last In Last Out
O(1) insert(), O(1) pop
ex: remember last element inserted
"""

stack = [] 
  
stack.append('a') 
stack.append('b') 
stack.append('c')
print(stack) 

print(f"popped: {stack.pop()}")
print(f"popped: {stack.pop()}")
print(f"popped: {stack.pop()}")

print(stack)


