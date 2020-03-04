"""
given a network grid, where 1 is already upgraded.
each night an 1 can update it's adjacent neighbors.
return how many days it takes to upgrad all to 1

input = [[0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]]

grid = [[11, 1, 1, 11, 1],
        [11, 1, 11, 1, 11],
        [12, 11, 12, 11, 1],
        [11, 1, 11, 12, 11]]

11 are converted on first day
12 are converted by 11 on the second day

"""

from pprint import pprint

grid = [[0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]]


def minimumDays(rows, column, grid):
    step = 0

    host_locations = []
    # find all day 1 1's
    for i in range(rows):
        for j in range(column):
            if grid[i][j] == 1:
                host_locations.append([i, j])
                print('added host location')

    # start expaning from host locations
    while len(host_locations) >0:
        increment = [0, 1, 0, -1, 0]
        for i in range(4):
            loc = host_locations.pop()
            print('current loc', loc)
            for i in range(len(increment)-1):
                newr = loc[0] + increment[i]
                newc = loc[1] - increment[i+1]

                # if neighbors not valid, or not 1, we ignore, we want to find all 0's and infect them
                # then put htem in queue
                if (newr < 0 or newr >= rows or newc < 0 or newc >= column or grid[newr][newc] == 1):
                    continue

                host_location.append([newr, newc])
                grid[newr, newc] = 1
                print('updated grid')

        step += 1
    print(step-1)
    pprint(grid)


minimumDays(len(grid), len(grid[0]), grid)
