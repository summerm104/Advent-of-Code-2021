def makeChunks(filename):
    with open(filename) as f:
        chunks = [line.strip() for line in f]
    return chunks

def findCorrupted(chunks):
    first_illegals = []
    open_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for chunk in chunks:
        stack = []
        for bracket in chunk:
            if bracket in open_dict:
                stack.append(bracket)
            else:
                last_open = stack.pop()
                if open_dict[last_open] != bracket:
                    first_illegals.append(bracket)
                    break
    return first_illegals

def totalPoints(first_illegals):
    points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total = 0
    for illegal in first_illegals:
        total += points_dict[illegal]
    return total


chunks = makeChunks('input1210.txt')
first_illegals = findCorrupted(chunks)
total = totalPoints(first_illegals)
print(total)