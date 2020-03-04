"""
given str = "clementisacap"
             
             cle metisaca
             012|345678|90                 
                have to stop at the prev value pos +1
                then 


                mentisac
                
                
             
"""

str1 = "clementisacap"


def longest_substring_without_repeat(word):

    last_seen = {}
    longest = [0, 1]
    start_idx = 0
    for idx, char in enumerate(word):
        
        print(idx,char)
        # always start the the biggest index possible
        if char in last_seen:
            start_idx = max(start_idx, last_seen[char] + 1)

        # we only updatet he word idx, when
        # the old longest length is less than
        # our current length, this can still increase
        if longest[1] - longest[0] < idx + 1 - start_idx:
            longest = [start_idx, idx+1]

        # always update the new char pos
        last_seen[char] = idx

    # the logest stores the starting and the last_idx+1
    return word[longest[0]:longest[1]]


res = longest_substring_without_repeat(str1)

print(res)