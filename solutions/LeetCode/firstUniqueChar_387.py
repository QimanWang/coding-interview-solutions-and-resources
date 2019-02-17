import collections
def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        print(count)
        print(type(count))
        # find the index
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1       
        return -1
        

print(firstUniqChar('aazycdd'))