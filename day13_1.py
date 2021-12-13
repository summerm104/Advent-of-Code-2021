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

def firstFold(map, instructions):
    instruction = instructions[0]
    fold_direct, fold_line = instruction[0], instruction[1]
    if fold_direct == 'y':
        folded_map = [coord for coord in map if coord[1] < fold_line]
        for coord in map:
            if coord[1] > fold_line:
                d = coord[1] - fold_line
                if coord[1]-d*2 >= 0:
                    folded_coord = [coord[0], coord[1]-d*2]
                    if folded_coord not in folded_map:
                        folded_map.append(folded_coord)
    else:
        folded_map = [coord for coord in map if coord[0] < fold_line]
        for coord in map:
            if coord[0] > fold_line:
                d = coord[0] - fold_line
                if coord[0]-d*2 >= 0:
                    folded_coord = [coord[0]-d*2, coord[1]]
                    if folded_coord not in folded_map:
                        folded_map.append(folded_coord)
    return len(folded_map)


data = makeMap('input1213.txt')
map = data[0]
instructions = data[1]
first_folded = firstFold(map, instructions)
print(first_folded)