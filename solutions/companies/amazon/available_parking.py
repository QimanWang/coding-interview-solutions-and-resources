"""
all 1's touching sdjacent is considered one block of parking space.
fine how many block of parkign space

input = [[1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1]]
after grouping = [[1, 1, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 0],
                [3, 0, 3, 3],
                [3, 3, 3, 3]]
"""

from pprint import pprint

grid = [[1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1]]

ans = [[10, 10, 0, 0],
       [0, 0, 11, 0],
       [0, 0, 0, 0],
       [12, 0, 12, 12],
       [12, 12, 12, 12]]
# every adjacent is consider a parking spot

res = 10


def numberAmaonTreasureTruck(rows, column, grid):
    global res
    for i in range(rows):
        for j in range(column):
            if grid[i][j] == 1:
                dfs(rows, column, grid, i, j)
                res += 1
                print('found one')

    print(res)
    pprint(grid)


def dfs(rows, column, grid, i, j):

    if (i < 0 or i >= rows or j < 0 or j >= column or grid[i][j] != 1):
        return

    pprint(grid)
    grid[i][j] = res
    
    dfs(rows, column, grid, i+1, j)
    dfs(rows, column, grid, i-1, j)
    dfs(rows, column, grid, i, j+1)
    dfs(rows, column, grid, i, j-1)


numberAmaonTreasureTruck(len(grid), len(grid[0]), grid)
