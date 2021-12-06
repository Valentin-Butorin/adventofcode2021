with open('day6_input.txt') as f:
    input_array = f.read().split(',')


def born_fish(_dict, count, max_n):
    for _ in range(count):
        max_n += 1
        _dict[max_n] = 8


def func(array, days):
    def counter(t):
        if t[1] == 0:
            cnt_array[0] += 1
            return t[0], 6
        return t[0], t[1] - 1

    fish_dict = {i: int(value) for i, value in enumerate(array)}

    for _ in range(days):
        cnt_array = [0]
        fish_dict = {key: value for key, value in map(lambda x: counter(x), fish_dict.items())}
        born_fish(fish_dict, cnt_array[0], len(fish_dict) - 1)

    print(len(fish_dict.keys()))


func(input_array, 80)
func(input_array, 256)
