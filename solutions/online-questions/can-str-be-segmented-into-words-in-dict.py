wordDict = set(['face','book','facebook'])
s='facebook'
def can_be_seperated(a,wordDict):
    n=len(s)
    can_seperate=[False for c in range(n+1)]
    print(can_seperate)

print(can_be_seperated(s,wordDict))