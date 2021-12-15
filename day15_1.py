# referenced from https://github.com/EfficientBogoSort/AOC2021/blob/main/Day%2015.py

from heapdict import heapdict

def makeGrid(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            row = [int(cell) for cell in list(line.strip())]
            grid.append(row)
    return grid

def findLeastRisk(grid):
    adjacent = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    visited = set()
    risk_level = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
    risk_level[0][0] = 0
    # priority queue
    que = heapdict()
    que[(0, 0)] = 0

    while len(que) > 0:
        # pop up the lowest accumulated risk level
        current, risk = que.popitem()
        i, j = current[0], current[1]
        visited.add(current)
        for direct in adjacent:
            neighbor = (current[0] + direct[0], current[1] + direct[1])
            x, y = neighbor[0], neighbor[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if neighbor not in visited:
                    new_risk = grid[x][y] + risk_level[i][j]
                    # check if the new accumulated risk level of the neighbor
                    # is smaller than the one stored previously
                    if new_risk < risk_level[x][y] or risk_level[x][y] == -1:
                        risk_level[x][y] = new_risk
                        que[neighbor] = new_risk
    return risk_level[-1][-1]


grid = makeGrid('input1215.txt')
min_risk = findLeastRisk(grid)
print(min_risk)