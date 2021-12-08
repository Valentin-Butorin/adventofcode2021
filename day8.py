from itertools import permutations

with open('day8_input.txt') as f:
    input_array = f.read().split('\n')


def first_part_func():
    count = 0

    for line in input_array:
        nums = line.split(' | ')[1]
        for num_str in nums.split(' '):
            if len(num_str) in [2, 3, 4, 7]:
                count += 1
    print(count)


def decode(lst):
    d = {
        'up': None,
        'rightup': None,
        'rightdown': None,
        'down': None,
        'leftdown': None,
        'leftup': None,
        'middle': None,
    }
    letters = 'abcdefg'
    dct = dict()

    for string in lst:
        if len(string) == 2:
            dct[1] = string
        elif len(string) == 3:
            dct[7] = string
        elif len(string) == 4:
            dct[4] = string
        elif len(string) == 7:
            dct[8] = string

    d['up'] = [s for s in dct[7] if s not in dct[1]][0]

    for string in lst:
        if string not in dct.values():
            for i in range(2):
                if 6 in dct.keys():
                    continue
                for el in permutations(dct[8].replace(dct[1][i], ''), len(dct[8].replace(dct[1][i], ''))):
                    if ''.join(el) == string:
                        dct[6] = string
                        break

    d['rightup'] = [s for s in dct[1] if s not in dct[6]][0]
    d['rightdown'] = dct[1].replace(d['rightup'], '')

    for string in lst:
        if string not in dct.values():
            target = dct[4].replace(dct[1][0], '').replace(dct[1][1], '')
            for i in range(2):
                if 0 in dct.keys():
                    continue
                for el in permutations(dct[8].replace(target[i], ''), len(dct[8].replace(target[i], ''))):
                    if ''.join(el) == string:
                        dct[0] = string
                        break

    d['middle'] = [s for s in dct[8] if s not in dct[0]][0]
    d['leftup'] = [s for s in dct[4] if s not in [d['rightup'], d['rightdown'], d['middle']]][0]

    for string in lst:
        if string not in dct.values():
            target = [s for s in letters if s not in d.values()]
            for i in range(2):
                if 9 in dct.keys():
                    continue
                for el in permutations(dct[8].replace(target[i], ''), len(dct[8].replace(target[i], ''))):
                    if ''.join(el) == string:
                        dct[9] = string
                        break

    d['leftdown'] = [s for s in dct[8] if s not in dct[9]][0]
    d['down'] = [s for s in letters if s not in d.values()][0]

    five = d['up'] + d['leftup'] + d['middle'] + d['rightdown'] + d['down']
    three = d['up'] + d['rightup'] + d['middle'] + d['rightdown'] + d['down']
    two = d['up'] + d['rightup'] + d['middle'] + d['leftdown'] + d['down']

    for el in permutations(five, len(five)):
        if ''.join(el) in lst:
            dct[5] = ''.join(el)
            break

    for el in permutations(three, len(three)):
        if ''.join(el) in lst:
            dct[3] = ''.join(el)
            break

    for el in permutations(two, len(two)):
        if ''.join(el) in lst:
            dct[2] = ''.join(el)
            break
    return dct


def second_part_func():
    result = 0

    for line in input_array:
        signals, outputs = line.split(" | ")[0].split(' '), line.split(" | ")[1].split(' ')
        d = decode(signals)
        num = ''
        for el in outputs:
            for lst in permutations(el, len(el)):
                string = ''.join(lst)
                if string in d.values():
                    for key, value in d.items():
                        if string == value:
                            num += str(key)
        if num:
            result += int(num)

    print(result)


first_part_func()
second_part_func()
