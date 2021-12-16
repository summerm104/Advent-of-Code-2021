# referenced from https://github.com/IdrisTheDragon/Advent2021/blob/main/day_16/day_16.py

def makePackets(hexa):
    bi_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111'}
    packets = ''
    for elem in hexa:
        packets += bi_dict[elem]
    return packets

def bi2deci(binary):
    # decimal = 0
    # binary = ''.join(list(binary)[::-1])
    # for i in range(len(binary)):
    #     decimal += int(binary[i]) * 2**i
    # return decimal
    return int(binary, 2)

total = 0
def parsePackets(packets):
    global total
    total += bi2deci(packets[:3])
    type_id = packets[3:6]
    if type_id == '100':
        i = 6
        lite_val = 0
        while True:
            lite_val += bi2deci(packets[i+1:i+5])
            if packets[i] == '0':
                break
            i += 5
        pack_len = i + 5
        return pack_len, lite_val
    else:
        bits_len = 0
        lite_vals = []
        len_id = packets[6]
        if len_id == '0':
            target_len = bi2deci(packets[7:7+15])
            while bits_len < target_len:
                pack_len, lite_val = parsePackets(packets[7+15+bits_len:])
                bits_len += pack_len
                lite_vals.append(lite_val)
            pack_len = 7 + 15 + bits_len
        else:
            subpack_num = bi2deci(packets[7:7+11])
            while subpack_num > 0:
                subpack_num -= 1
                pack_len, lite_val = parsePackets(packets[7+11+bits_len:])
                bits_len += pack_len
                lite_vals.append(lite_val)
            pack_len = 7 + 11 + bits_len
        return pack_len, lite_val


with open('input1216.txt') as f:
    hexa = f.readline().strip()
packets = makePackets(hexa)
parsePackets(packets)
print(total)