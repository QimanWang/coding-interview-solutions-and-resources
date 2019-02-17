class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        height = len(matrix)
        width = len(matrix[0])
        
        dp = [[0]*width for _ in range(height)]

        max_size = 0
        
        for r in range(0,height):
            for c in range(0,width):
                # if 0, go to next cell
                if matrix[r][c] !='0':
                    
                    # print(type(matrix[r][c]))
                    dp[r][c]=1
                    
                    
                    if c > 0 and r > 0:
                        left = int(matrix[r][c-1]) 
                        top = int(matrix[r-1][c]) 
                        top_left = int(matrix[r-1][c-1]) 
                        dp[r][c] = min(left + 1, top+1, top_left+1)
                    
                    
                    if max_size < dp[r][c]:
                        max_size = dp[r][c]

                    for r in range(0,len(dp)):
                        print(dp[r])
            return max_size * max_size
    
    

matrix = [["1","1","1","1"],
["1","1","1","1"],
["1","1","1","1"]]
s = Solution()
print(s.maximalSquare(matrix))

        
        
         