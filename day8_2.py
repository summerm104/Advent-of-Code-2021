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

def getEntryCode(display):
    entry_code = ''
    solved = {}
    key_seg = {}
    inputs, outputs = display[0], display[1]
    for digit in inputs:
        sorted_digit = ''.join(sorted(digit))
        if len(digit) == 2:
            solved[sorted_digit] = 1
            key_seg['cf'] = list(digit)
        elif len(digit) == 3:
            solved[sorted_digit] = 7
        elif len(digit) == 4:
            solved[sorted_digit] = 4
            key_seg['bdcf'] = list(digit)
        elif len(digit) == 7:
            solved[sorted_digit] = 8
    key_seg['bd'] = [seg for seg in key_seg['bdcf'] if seg not in key_seg['cf']]
    
    unsolved = [digit for digit in inputs if len(digit) == 6 or len(digit) == 5]
    for digit in unsolved:
        digit_li = list(digit)
        sorted_digit = ''.join(sorted(digit))
        key1 = len([seg for seg in digit_li if seg in key_seg['cf']])
        key2 = len([seg for seg in digit_li if seg in key_seg['bd']])
        if len(digit) == 6:
            if key1 == 1 and key2 == 2:
                solved[sorted_digit] = 6
            elif key1 == 2 and key2 == 1:
                solved[sorted_digit] = 0
            else:
                solved[sorted_digit] = 9
        else:
            if key1 == 1 and key2 == 1:
                solved[sorted_digit] = 2
            elif key1 == 2 and key2 == 1:
                solved[sorted_digit] = 3
            else:
                solved[sorted_digit] = 5
    for digit in outputs:
        sorted_digit = ''.join(sorted(digit))
        num = str(solved[sorted_digit])
        entry_code += num
    return entry_code

def countTotal(displays):
    total = 0
    for display in displays:
        entry_code = getEntryCode(display)
        total += int(entry_code)
    return total


displays = getDisplays('input1208.txt')
total = countTotal(displays)
print(total)