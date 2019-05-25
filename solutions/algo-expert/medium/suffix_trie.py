# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
            self.populateSubStringStartingAt(i,string)

    def populateSubStringStartingAt(self,i,string):
        node = self.root
        for j in range(i,len(string)):
            letter = string[j]
            if letter not in node:
                node[letter]={}
            node = node[letter]
        # mark end of string
        node[self.endSymbol] = True
        
        
    def contains(self, string):
        node = self.root
        for car in string:
            if car not in node:
                return False
            node = node[car]
        
        return True if self.endSymbol in node else False
    
    def print_tree(self):
        for key,val in self.root.items():
            print(key,val)

s = 'babc'

t = SuffixTrie(s)
t.print_tree()