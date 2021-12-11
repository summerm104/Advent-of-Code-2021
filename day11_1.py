def makeGrid(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append(list(line.strip()))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = int(grid[i][j])
    return grid

def countFlashes(grid, steps):
    flashes = 0
    adjacent = [(-1,0), (-1,-1), (-1,1), (0,-1), (0,1), (1,0), (1,-1), (1,1)]
    while steps > 0:
        visited = set()
        unvisited = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    visited.add((i,j))
                    for elem in adjacent:
                        x = i + elem[0]
                        y = j + elem[1]
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            grid[x][y] += 1
                            if grid[x][y] > 9 and (x,y) not in visited and (x,y) not in unvisited:
                                if elem in [(-1,0), (-1,-1), (-1,1), (0,-1)]:
                                    unvisited.append((x,y))

        while len(unvisited) > 0:
            octopus = unvisited.pop(0)
            visited.add(octopus)
            i, j = octopus[0], octopus[1]
            for elem in adjacent:
                x = i + elem[0]
                y = j + elem[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    grid[x][y] += 1
                    if grid[x][y] > 9 and (x,y) not in visited and (x,y) not in unvisited:
                            unvisited.append((x,y))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9:
                    grid[i][j] = 0
                    flashes += 1
        steps -= 1
    return flashes

grid = makeGrid('input1211.txt')
flashes = countFlashes(grid, 100)
print(flashes)