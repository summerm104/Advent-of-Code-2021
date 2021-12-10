def makeChunks(filename):
    with open(filename) as f:
        chunks = [line.strip() for line in f]
    return chunks

def findIncomplete(chunks):
    res = chunks.copy()
    open_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for chunk in chunks:
        stack = []
        for bracket in chunk:
            if bracket in open_dict:
                stack.append(bracket)
            else:
                last_open = stack.pop()
                if open_dict[last_open] != bracket:
                    res.remove(chunk)
                    break
    return res

def makeComplete(incomplete_chunks):
    open_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    res = []
    for chunk in incomplete_chunks:
        stack = []
        completes = ''
        for bracket in chunk:
            if bracket in open_dict:
                stack.append(bracket)
            else:
                stack.pop()
        stack = stack[::-1]
        for open_bracket in stack:
            completes += open_dict[open_bracket]
        res.append(completes)
    return res

def findMiddlePoint(completes):
    point_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    points = []
    for brackets in completes:
        total = 0
        for bracket in brackets:
            total *= 5
            total += point_dict[bracket]
        points.append(total)
    points.sort()
    return points[int((len(points)-1)/2)]

chunks = makeChunks('input1210.txt')
incomplete_chunks = findIncomplete(chunks)
completes = makeComplete(incomplete_chunks)
middle_point = findMiddlePoint(completes)
print(middle_point)