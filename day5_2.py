def getEndCoordinates(filename):
    res = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            coordinates = []
            for elem in line.split(' -> '):
                coordinates.append(elem.split(','))
            res.append(coordinates.copy())
    return res

def getAllCoordinates(end_coords):
    res = []
    for end_coord in end_coords:
        coords = []
        x1, y1 = int(end_coord[0][0]), int(end_coord[0][1])
        x2, y2 = int(end_coord[1][0]), int(end_coord[1][1])
        # horizontal
        if x1 == x2:
            x = x1
            if y1 < y2:
                for y in range(y1, y2+1):
                    coords.append((x,y))
            else:
                for y in range(y2, y1+1):
                    coords.append((x,y))
            res.append(coords.copy())
        # vertical
        if y1 == y2:
            y = y1
            if x1 < x2:
                for x in range(x1, x2+1):
                    coords.append((x,y))
            else:
                for x in range(x2, x1+1):
                    coords.append((x,y))
            res.append(coords.copy())
        # diagonal
        if abs(x1-x2) == abs(y1-y2):
            x = x1
            y = y1
            coords.append((x,y))
            if x1 < x2 and y1 < y2:
                while x < x2:
                    x += 1
                    y += 1
                    coords.append((x,y))
            elif x1 < x2 and y1 > y2:
                while x < x2:
                    x += 1
                    y -= 1
                    coords.append((x,y))
            elif x1 > x2 and y1 < y2:
                while x > x2:
                    x -= 1
                    y += 1
                    coords.append((x,y))
            elif x1 > x2 and y1 > y2:
                while x > x2:
                    x -= 1
                    y -= 1
                    coords.append((x,y))
            res.append(coords.copy())
    return res

def countCoordinates(all_coords):
    count_dict = {}
    count_points = 0
    for coords in all_coords:
        for coord in coords:
            if coord not in count_dict:
                count_dict[coord] = 1
            else:
                count_dict[coord] += 1
    for k in count_dict:
        if count_dict[k] > 1:
            count_points += 1
    return count_points


end_coords = getEndCoordinates('input1205.txt')
all_coords = getAllCoordinates(end_coords)
count_points = countCoordinates(all_coords)
print(count_points)