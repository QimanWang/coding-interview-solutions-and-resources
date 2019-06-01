def minRewards(scores):
    # Write your code here.
    min_score_idx = findSmallest(scores)

    # now we can expand out from there
    # assign rewards left
    i = min_score_idx -1
    left_reward = 0
    curr_reward = 0
    while i > 0:
        if scores[i] > scores[i-1]:
            curr_reward+=1
        else:
            curr_reward = max(1,curr_reward-scores[i-1]-scores[i])
            
        
        left_reward += curr_reward

        i-=1

    # assign rewards right
    j=min_score_idx+1
    right_reward = 0
    curr_reward = 0
    while j < len(scores):
        if scores[j] > scores[j-1]:
            curr_reward+=1
        else:
            curr_reward = max(1,curr_reward-scores[i-1]-scores[i])

        right_reward += curr_reward
         
        j+=1
    return left_reward + right_reward


def findSmallest(scores):
    min_score = scores[0]
    min_score_idx = 0
    for i in range(1,len(scores)):
        if scores[i] < min_score:
            min_score=scores[i]
            min_score_idx = i
    return min_score_idx
                

ary =[8,4,2,1,3,6,7,9,5]
print(minRewards(ary))
