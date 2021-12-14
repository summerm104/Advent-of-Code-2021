def makeTemplate(filename):
    rules = {}
    with open(filename) as f:
        template = f.readline().strip()
        for line in f:
            if '->' in line:
                [pair, insert] = line.strip().split(' -> ')
                rules[pair] = insert
    return template, rules

def countPolyGap(template, rules, steps):
    start = template[0]
    end = template[-1]
    current_pair_dict = {pair: 0 for pair in rules.keys()}
    for i in range(len(template) - 1):
        current_pair_dict[template[i:i+2]] += 1
    # print({pair:count for pair,count in current_pair_dict.items() if count > 0})
    # generate new pairs
    while steps > 0:
        steps -= 1
        new_pair_dict = {pair: 0 for pair in rules.keys()}
        for pair, count in current_pair_dict.items():
            new_pair_dict[pair[0]+rules[pair]] += count
            new_pair_dict[rules[pair]+pair[1]] += count
        current_pair_dict = new_pair_dict
    
    # tempt = {pair:count for pair,count in new_pair_dict.items() if count > 0}
    # print(tempt)
    
    # count each element
    elem_count = {}
    for pair, count in new_pair_dict.items():
        if pair[0] not in elem_count:
            elem_count[pair[0]] = 0
        if pair[1] not in elem_count:
            elem_count[pair[1]] = 0
        elem_count[pair[0]] += count
        elem_count[pair[1]] += count
    elem_count[start] += 1
    elem_count[end] += 1
    real_elem_count = {elem: count//2 for elem, count in elem_count.items()}
    # print(elem_count)
    # print(real_elem_count)

    counts = list(real_elem_count.values())

    return max(counts) - min(counts)


data = makeTemplate('input1214.txt')
template = data[0]
rules = data[1]
res = countPolyGap(template, rules, 40)
print(res)