def str2list(data):
    res = []
    for line in data:
        direc = line.strip().split(' ')
        res.append(direc)
    return res

def position(direcs):
    hrz = 0
    depth = 0
    aim = 0
    for direc in direcs:
        if direc[0] == 'forward':
            hrz += int(direc[1])
            depth += aim * int(direc[1])
        elif direc[0] == 'down':
            aim += int(direc[1])
        elif direc[0] == 'up':
            aim -= int(direc[1])
    res = hrz * depth
    return res

data = open('input1202.txt')
direcs = str2list(data)
print(position(direcs))