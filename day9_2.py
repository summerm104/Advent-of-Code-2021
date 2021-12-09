def makeMap(filename):
    map = []
    with open(filename) as f:
        for line in f:
            row = [int(height) for height in list(line.strip())]
            map.append(row.copy())
    return map

def findLowPoints(map):
    low_points = []
    adjacent = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(len(map)):
        for j in range(len(map[i])):
            neighbors = []
            for elem in adjacent:
                x = i + elem[0]
                y = j + elem[1]
                if 0 <= x < len(map) and 0 <= y < len(map[0]):
                    neighbors.append(map[x][y])
            if min(neighbors) > map[i][j]:
                low_points.append((i, j))
    return low_points

def findBasins(map, low_points):
    visited = set()
    adjacent = [(1,0), (-1,0), (0,1), (0,-1)]
    not_basin = 9
    basins = []
    for low_point in low_points:
        stack = [low_point]
        visited.add(low_point)
        basin_size = 1
        while len(stack) > 0:
            current = stack.pop()
            i, j = current[0], current[1]
            for elem in adjacent:
                x = i + elem[0]
                y = j + elem[1]
                if 0 <= x < len(map) and 0 <= y < len(map[0]):
                    if map[x][y] != not_basin and (x, y) not in visited:
                        stack.append((x, y))
                        visited.add((x, y))
                        basin_size += 1
        basins.append(basin_size)
    return basins

def threeLarBasins(basins):
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]

map = makeMap('input1209.txt')
low_points = findLowPoints(map)
basins = findBasins(map, low_points)
res = threeLarBasins(basins)
print(res)