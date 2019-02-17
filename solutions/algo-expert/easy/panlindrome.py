def isPalindrome(string):
    # Write your code here.
    '''
    palindrome is a string that is same forward and backwards
    racecar

    two pointer, 0, len(str)
    if match char at both position, we will move pointer inwards by 1
    '''

    left, right = 0, len(string)-1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True
