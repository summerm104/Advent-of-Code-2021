def makeMap(filename):
    with open(filename) as f:
        lines = f.readlines()
        map = [line.strip().split(',') for line in lines if not line.startswith('fold') and line != '\n']
        instructions = [line.strip().split('=') for line in lines if line.startswith('fold')]
        for coord in map:
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
        for instruction in instructions:
            instruction[0] = instruction[0][-1]
            instruction[1] = int(instruction[1])
    return map, instructions

def makeFoldedMap(map, instructions):
    current_map = map
    for instruction in instructions:
        fold_direct, fold_line = instruction[0], instruction[1]
        if fold_direct == 'y':
            folded_map = [coord for coord in current_map if coord[1] < fold_line]
            for coord in current_map:
                if coord[1] > fold_line:
                    d = coord[1] - fold_line
                    if coord[1]-d*2 >= 0:
                        folded_coord = [coord[0], coord[1]-d*2]
                        if folded_coord not in folded_map:
                            folded_map.append(folded_coord)
        else:
            folded_map = [coord for coord in current_map if coord[0] < fold_line]
            for coord in current_map:
                if coord[0] > fold_line:
                    d = coord[0] - fold_line
                    if coord[0]-d*2 >= 0:
                        folded_coord = [coord[0]-d*2, coord[1]]
                        if folded_coord not in folded_map:
                            folded_map.append(folded_coord)
        current_map = folded_map
    return folded_map

def makeCodeGraph(folded_map):
    max_x = max([coord[0] for coord in folded_map])
    max_y = max([coord[1] for coord in folded_map])
    graph = []
    # make a blank graph
    for i in range(max_y + 1):
        row = []
        for j in range(max_x + 1):
            row.append('.')
        graph.append(row)
    # mark coordinates in the graph
    for coord in folded_map:
        i, j = coord[1], coord[0]
        graph[i][j] = '#'
    for i in range(len(graph)):
        graph[i] = ''.join(graph[i])
    return graph
    

data = makeMap('input1213.txt')
map = data[0]
instructions = data[1]
folded_map = makeFoldedMap(map, instructions)
graph = makeCodeGraph(folded_map)
for row in graph:
    print(row)