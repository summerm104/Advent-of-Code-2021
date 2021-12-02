def str2list(data):
    res = []
    for line in data:
        num = int(line.strip())
        res.append(num)
    return res

def threeMeasurement(li):
    count = 0
    for i in range(len(li) - 3):
        if li[i + 3] > li[i]:
            count += 1
    return count

data = open("input1201.txt")
num_list = str2list(data)
three_incre = threeMeasurement(num_list)
print(three_incre)