# Feel free to add new properties and methods to the class.
class MinMaxStack:
    s = []
    min =float('INF')
    max = float('-INF')
    def peek(self):
        # Write your code here.
        if len(s) > 0:
            return s[-1]
        else:
            return None
 
    def pop(self):
        # Write your code here.
        s.pop()

    def push(self, number):
        # Write your code here.
        s.append(number)

    def getMin(self):
        # Write your code here.
        


    def getMax(self):
        # Write your code here.

