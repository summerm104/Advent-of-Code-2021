def str2list(filename):
    with open(filename) as f:
        fishes = f.readline().split(',')
    for i in range(len(fishes)):
        fishes[i] = int(fishes[i])
    return fishes

def countFish(fishes, days):
    current = fishes
    while days > 0:
        another_day = current.copy()
        for i in range(len(current)):
            if current[i] == 0:
                another_day[i] = 6
                another_day.append(8)
            else:
                another_day[i] = current[i] - 1
        current = another_day.copy()
        days -= 1
    return current


fishes = str2list('input1206.txt')
current = countFish(fishes, 80)
print(current)