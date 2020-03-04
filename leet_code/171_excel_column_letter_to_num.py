
def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    
    letter * (26* n) + .... + letter * (26* 1) + letter * (26 * 0)
    
    """
    i = len(s)-1
    sum = 0
    for letter in s:
        # letter * (26* n)
        sum += (ord(letter) - 64) * (26**i)
        i-=1
    return sum


        