from collections import Counter, defaultdict

with open('day9_input.txt') as f:
    input_array = f.read().split('\n')
    input_array = list(map(lambda x: [int(y) for y in x], input_array))


def first_part_func(array):
    result = 0
    for i, line in enumerate(array):
        for j in range(len(line)):
            point = line[j]
            up = True
            down = True
            left = True
            right = True
            if i == 0:
                up = False
            if i == len(array) - 1:
                down = False
            if j == 0:
                left = False
            if j == len(line) - 1:
                right = False
            if up and point >= array[i - 1][j]:
                continue
            if down and point >= array[i + 1][j]:
                continue
            if left and point >= line[j - 1]:
                continue
            if right and point >= line[j + 1]:
                continue

            result += point + 1

    print(result)


def get_grid(arr):
    c = defaultdict()

    for y in range(len(arr)):
        c[(-1, y)] = 0
        c[(len(arr[0]), y)] = 0

    for x in range(len(arr[0])):
        c[(x, -1)] = 0
        c[(x, len(arr))] = 0

    for y, line in enumerate(arr):
        for x, value in enumerate(line):
            c[(x, y)] = value
    return c


def second_part_func(array):
    counter = Counter()
    coords = get_grid(array)

    for (x, y), value in coords.items():
        if 0 <= x < len(array[0]) and 0 <= y < len(array) and value != 9:
            while 0 <= x < len(array[0]) and 0 <= y < len(array):
                for step_x, step_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if coords[x + step_x, y + step_y] < coords[x, y]:
                        x += step_x
                        y += step_y
                        break
                else:
                    counter[x, y] += 1
                    break

    a, b, c = counter.most_common(3)
    print(a[1] * b[1] * c[1])


first_part_func(input_array)
second_part_func(input_array)
