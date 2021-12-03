def str2list(data):
    res = []
    for line in data:
        bi = line.strip()
        res.append(bi)
    return res

def gammaRate(bi_list):
    count_one = {}
    count_total = len(bi_list)
    gamma = ''
    for elem in bi_list:
        for i in range(len(elem)):
            if elem[i] == '1':
                if i not in count_one:
                    count_one[i] = 1
                else:
                    count_one[i] += 1
    
    for i in range(len(bi_list[0])):
        if i not in count_one:
            gamma += '0'
        elif count_one[i] > count_total - count_one[i]:
            gamma += '1'
        else:
            gamma += '0' 
    return gamma

def bi2deci(bi_str):
    res = 0
    bi_str = bi_str[::-1]
    for i in range(len(bi_str)):
        res += int(bi_str[i]) * (2**i)
    return res

def powerComsump(gamma):
    epsilon = ''
    for s in gamma:
        if s == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    gamma_d = bi2deci(gamma)
    epsilon_d = bi2deci(epsilon)
    comsump = gamma_d * epsilon_d
    return comsump

data = open('input1203.txt')
bi_list = str2list(data)
gamma = gammaRate(bi_list)
power_comsump = powerComsump(gamma)
print(power_comsump)

    