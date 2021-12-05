from collections import Counter

with open('day5_input.txt') as f:
    input_array = list(map(lambda x: x.split(' -> '), f.read().split('\n')))
    input_array = [[[int(el1) for el1 in el[0].split(',')], [int(el1) for el1 in el[1].split(',')]] for el in
                   input_array]

print(input_array)


def first_part_func(L):
    a1, b1 = L[0]
    a2, b2 = L[1]
    if a1 == a2:
        if b1 < b2:
            b1, b2 = b2, b1

        while b1 >= b2:
            points.append((a1, b1))
            b1 -= 1
    elif b1 == b2:
        if a1 < a2:
            a1, a2 = a2, a1

        while a1 >= a2:
            points.append((a1, b1))
            a1 -= 1


points = []
for el in input_array:
    x1, y1 = el[0]
    x2, y2 = el[1]
    if x1 == x2 or y1 == y2:
        first_part_func([(x1, y1), (x2, y2)])

counter = Counter(points)
print(len([num for num in counter.values() if num > 1]))


def second_part_func(L):
    a1, b1 = L[0]
    a2, b2 = L[1]
    if a1 == a2:
        if b1 < b2:
            b1, b2 = b2, b1

        while b1 >= b2:
            points.append((a1, b1))
            b1 -= 1
    elif b1 == b2:
        if a1 < a2:
            a1, a2 = a2, a1

        while a1 >= a2:
            points.append((a1, b1))
            a1 -= 1
    else:
        a_step = -1 if a1 > a2 else 1
        b_step = -1 if b1 > b2 else 1

        while a1 != a2 and b1 != b2:
            points.append((a1, b1))
            a1 += a_step
            b1 += b_step
        else:
            points.append((a1, b1))


points = []
for el in input_array:
    x1, y1 = el[0]
    x2, y2 = el[1]
    second_part_func([(x1, y1), (x2, y2)])

counter = Counter(points)
print(len([num for num in counter.values() if num > 1]))
