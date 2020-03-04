def riverSizes(matrix):
    sizes  = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(i,j)
            
            # do bfs
            sizes.append(bfs(matrix,i,j,0))
        
    return sizes

def bfs(matrix,i,j,size):



matrix = [[1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 0]]

res = riverSizes(matrix)

print(res)
