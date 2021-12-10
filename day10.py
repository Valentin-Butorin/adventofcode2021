from statistics import median

with open('day10_input.txt') as f:
    input_array = f.read().split('\n')


def first_part_func(array):
    score_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    result = 0
    for line in array:
        string = delete_pairs(line)
        result += get_score(string, score_dict)
    print(result)


def get_score(input_string, score_dict):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    result_sum = 0
    lst = []
    for char in input_string:
        if char in pairs.keys():
            lst.append(char)
        elif lst.pop(-1) != (key for key, value in pairs.items() if value == char).__next__():
            result_sum += score_dict[char]
            break

    return result_sum


def delete_pairs(string):
    result = string.replace('[]', '').replace('()', '').replace('<>', '').replace('{}', '')
    while True:
        temp = result.replace('[]', '').replace('()', '').replace('<>', '').replace('{}', '')
        if len(temp) == len(result):
            return result
        result = temp


def is_defective(input_str):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    lst = []
    for char in input_str:
        if char in pairs.keys():
            lst.append(char)
        elif lst.pop(-1) != (key for key, value in pairs.items() if value == char).__next__():
            return True
    return False


def repair(input_str):
    result_sum = 0
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    lst = []
    for char in input_str:
        if char in pairs.keys():
            lst.append(char)

    for el in reversed(lst):
        result_sum = result_sum * 5 + scores[pairs[el]]
    return result_sum


def second_part_func(array):
    lst = []
    for line in array:
        line = delete_pairs(line)
        if not is_defective(line):
            lst.append(repair(line))

    lst.sort()
    print(median(lst))


first_part_func(input_array)
second_part_func(input_array)
