'''
we have to match bracket types.
what are the possible cases?
[] {} () 
'''
def balancedBrackets(string):
    s = []
    left ='{[('
    right = '}])'
    for c in string:
        if c in left:
            for idx in range(len(left)):
                if left[idx] == c:
                    s.append(right[idx])
                    break
        else:
            if len(s)==0 or s.pop() != c :
                return False
	return len(s)==0


                
    
        
            
        
        

        
