def makeMap(filename):
    map = []
    with open(filename) as f:
        for line in f:
            row = [int(height) for height in list(line.strip())]
            map.append(row.copy())
    return map

def totalRiskLevel(map):
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
                low_points.append(map[i][j])
    risk_levels = [low_point + 1 for low_point in low_points]
    total_risk_level = sum(risk_levels)
    return total_risk_level


map = makeMap('input1209.txt')
total_risk_level = totalRiskLevel(map)
print(total_risk_level)