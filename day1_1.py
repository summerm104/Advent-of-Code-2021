def str2list(data):
    res = []
    for line in data:
        num = int(line.strip())
        res.append(num)
    return res

def countIncrease(num_list):
    count = 0
    for i in range(len(num_list) - 1):
        if num_list[i+1] > num_list[i]:
            count += 1
    return count

data = open("input1201.txt")
num_list = str2list(data)
incre_count = countIncrease(num_list)
print(incre_count)

