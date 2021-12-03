def str2list(data):
    res = []
    for line in data:
        bi = line.strip()
        res.append(bi)
    return res

def bi2deci(bi_str):
    res = 0
    bi_str = bi_str[::-1]
    for i in range(len(bi_str)):
        res += int(bi_str[i]) * (2**i)
    return res

def generatorRating(bi_list, type):
    i = 0
    res = bi_list.copy()
    store_one = []
    store_zero = []
    while len(res) > 1:
        for bi in res:
            if bi[i] == '1':
                store_one.append(bi)
            else:
                store_zero.append(bi)
        if type == 'oxygen':
            if len(store_one) >= len(store_zero):
                res = store_one.copy()
            else:
                res = store_zero.copy()
        else:
            if len(store_one) >= len(store_zero):
                res = store_zero.copy()
            else:
                res = store_one.copy()
        i += 1
        store_one = []
        store_zero = []
    return res[0]

data = open('input1203.txt')
bi_list = str2list(data)
o2_bi = generatorRating(bi_list, 'oxygen')
co2_bi = generatorRating(bi_list, 'co2')
o2_deci = bi2deci(o2_bi)
co2_deci = bi2deci(co2_bi)
print(o2_deci * co2_deci)

