with open('day3_input.txt') as f:
    input_array = f.read().split('\n')


def diag_func(array):
    common = ''
    uncommon = ''
    length = len(array)

    for i in range(len(array[0])):
        col = list(map(lambda x: x[i], array))
        if col.count('0') > length // 2:
            common += '0'
            uncommon += '1'
        else:
            common += '1'
            uncommon += '0'

    return common, uncommon


def oxygen_func(num, array):
    for i in range(len(array[0])):
        cnt = list(map(lambda x: x[i], array)).count(str(num))

        if cnt > len(array) / 2:
            array = list(filter(lambda x: True if x[i] == '1' else False, array))
        elif cnt < len(array) / 2:
            array = list(filter(lambda x: True if x[i] == '0' else False, array))
        else:
            array = list(filter(lambda x: True if x[i] == str(num) else False, array))

        if len(array) == 1:
            return array[0]

        if len(array) == 2:
            return array[0] if array[0][-1] == str(num) else array[1]


gamma_rate, epsilon_rate = diag_func(input_array)
print(int(gamma_rate, 2) * int(epsilon_rate, 2))

rating = oxygen_func(1, input_array[:])
scrubber = oxygen_func(0, input_array[:])
print(int(rating, 2) * int(scrubber, 2))
