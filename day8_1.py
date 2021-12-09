def getDisplays(filename):
    res = []
    with open(filename) as f:
        for line in f:
            tempt = []
            line_li = line.strip().split(' | ')
            for elem in line_li:
                tempt.append(elem.split(' '))
            res.append(tempt.copy())
    return res

def countSimpleSeg(displays):
    count = 0
    out_index = 1
    simple_seg = [2, 3, 4, 7]
    for display in displays:
        for elem in display[out_index]:
            if len(elem) in simple_seg:
                count += 1
    return count


displays = getDisplays('input1208.txt')
count_simple = countSimpleSeg(displays)
print(count_simple)