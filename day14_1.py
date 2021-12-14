def makeTemplate(filename):
    rules = {}
    with open(filename) as f:
        template = f.readline().strip()
        for line in f:
            if '->' in line:
                [pair, insert] = line.strip().split(' -> ')
                rules[pair] = insert
    return template, rules

def makeNewPoly(template, rules, steps):
    current_poly = template
    while steps > 0:
        new_poly = ''
        for i in range(len(current_poly) - 1):
            pair = current_poly[i] + current_poly[i+1]
            insert = rules[pair]
            new_poly += current_poly[i] + insert
        new_poly += current_poly[-1]
        current_poly = new_poly
        steps -= 1
    return new_poly

def countRes(new_poly):
    count_dict = {}
    for elem in new_poly:
        count = new_poly.count(elem)
        if elem not in count_dict:
            count_dict[elem] = count
    max_count = max(list(count_dict.values()))
    min_count = min(list(count_dict.values()))
    return max_count - min_count


data = makeTemplate('input1214.txt')
template = data[0]
rules = data[1]
new_poly = makeNewPoly(template, rules, 10)
res = countRes(new_poly)
print(res)