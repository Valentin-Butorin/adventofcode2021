with open('day7_input.txt') as f:
    input_array = list(map(int, f.read().split(',')))


def first_part_func(array):
    fuel_arr = []
    for i in range(max(array)):
        total_fuel = 0
        for pos in array:
            if pos == i:
                continue
            elif pos > i:
                total_fuel += pos - i
            elif pos < i:
                total_fuel += i - pos
        fuel_arr.append(total_fuel)
    print(min(fuel_arr))


def second_part_func(array):
    fuel_arr = []
    for i in range(max(array)):
        total_fuel = 0
        for pos in array:
            if pos == i:
                continue
            elif pos > i:
                total_fuel += sum(range(1, pos - i + 1))
            elif pos < i:
                total_fuel += sum(range(1, i - pos + 1))
        fuel_arr.append(total_fuel)
    print(min(fuel_arr))


first_part_func(input_array)
second_part_func(input_array)
