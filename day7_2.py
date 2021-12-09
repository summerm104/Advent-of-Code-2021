def makeCrabDict(filename):
    crab_dict = {}
    with open(filename) as f:
        crabs = f.readline().split(',')
    for crab in crabs:
        crab_int = int(crab)
        if crab_int not in crab_dict:
            crab_dict[crab_int] = 0
        crab_dict[crab_int] += 1
    return crab_dict

def countFuel(steps):
    total = 0
    for num in range(steps + 1):
        total += num
    return total

def countCrabSteps(crab_dict):
    res = []
    crabs = list(crab_dict.items())
    for align_crab in crabs:
        align = align_crab[0]
        total = 0
        for crab in crabs:
            steps = countFuel(abs(crab[0] - align)) * crab[1]
            total += steps
        res.append(total)
    return res


crab_dict = makeCrabDict('input1207.txt')
crab_steps = countCrabSteps(crab_dict)
min_step = min(crab_steps)
print(min_step)