from copy import deepcopy

with open('day11_input.txt') as f:
    input_array = f.read().split('\n')
    input_array = list(map(lambda x: [int(z) for z in x], input_array))


def first_part_func(array, steps, get_first_sync=False):
    count = 0
    for step in range(steps):
        flash_coords = []
        for i, a in enumerate(array):
            for j, num in enumerate(a):
                array[i][j] += 1
                if array[i][j] == 10:
                    count += flash(array, (i, j))
                    array[i][j] += 1
        reset(array)
    print(count)


def flash(array, coords):
    i, j = coords
    cnt = 1
    steps = ((1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1))
    for step_x, step_y in steps:
        y, x = i + step_y, j + step_x
        if 0 <= x < 10 and 0 <= y < 10:
            array[y][x] += 1
            if array[y][x] == 10:
                cnt += flash(array, (y, x))
                array[y][x] += 1
    return cnt


def reset(array):
    for i, a in enumerate(array):
        for j, num in enumerate(a):
            if num > 9:
                array[i][j] = 0


def synchronized(array):
    if list(filter(lambda x: True if list(filter(lambda x: False if x == 1 else True, x)) else False, array)):
        return False
    return True


def second_part_func(array):
    def fl(array, coords, lst):
        i, j = coords
        lst[i][j] = 1
        cnt = 1
        steps = ((1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1))
        for step_x, step_y in steps:
            y, x = i + step_y, j + step_x
            if 0 <= x < 10 and 0 <= y < 10:
                array[y][x] += 1
                if array[y][x] == 10:
                    cnt += fl(array, (y, x), lst)
                    array[y][x] += 1
        return cnt

    step = 0
    while True:
        step += 1
        count = 0
        lst = [[0 for _ in range(10)] for _ in range(10)]
        for i, a in enumerate(array):
            for j, num in enumerate(a):
                array[i][j] += 1
                if array[i][j] == 10:
                    count += fl(array, (i, j), lst)
                    array[i][j] += 1
        reset(array)
        if synchronized(lst):
            print(step)
            break


first_part_func(deepcopy(input_array), 100)
second_part_func(deepcopy(input_array))
