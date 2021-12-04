from copy import deepcopy

with open('day4_input.txt') as f:
    input_array = list(
        map(lambda x: list(map(lambda y: list(filter(lambda z: z if z else None, y.split(' '))), x.split('\n'))),
            f.read().split('\n\n')))

nums = [18, 99, 39, 89, 0, 40, 52, 72, 61, 77, 69, 51, 30, 83, 20, 65, 93, 88, 29, 22, 14, 82, 53, 41, 76, 79, 46, 78,
        56, 57, 24, 36, 38, 11, 50, 1, 19, 26, 70, 4, 54, 3, 84, 33, 15, 21, 9, 58, 64, 85, 10, 66, 17, 43, 31, 27, 2,
        5, 95, 96, 16, 97, 12, 34, 74, 67, 86, 23, 49, 8, 59, 45, 68, 91, 25, 48, 13, 28, 81, 94, 92, 42, 7, 37, 75, 32,
        6, 60, 63, 35, 62, 98, 90, 47, 87, 73, 44, 71, 55, 80]

nums = list(map(lambda x: str(x), nums))


def first_part(arr):
    def check(numbers, arr):
        numbers = list(map(lambda x: str(x), numbers))
        for num in numbers:
            for i, board in enumerate(arr[:]):
                for j, line in enumerate(board):
                    if num in line:
                        arr[i][j].remove(num)
                        if not arr[i][j]:
                            return int(num), arr.pop(i)

    def get_first_winner(array):
        for i in range(0, len(nums), 5):
            winner_board = check(nums[i:i + 5], array)
            if winner_board:
                return winner_board

    winner_num, winner = get_first_winner(arr)

    sum_unchecked = 0
    for lst in winner:
        if lst:
            sum_unchecked += sum(map(lambda x: int(x), lst))

    print(winner_num * sum_unchecked)


def get_all_winners(array):
    result = []
    for num in nums:
        winner_board = check_all_winners(num, array)
        if winner_board:
            result.extend(winner_board)
    return result


def check_all_winners(number, array):
    winners = []
    mark_num(number, array)

    while True:
        winner_board = get_winner(array)
        if winner_board:
            winners.append([int(number), winner_board])
        else:
            break

    return winners


def mark_num(num, array):
    for i, board in enumerate(array):
        for j, line in enumerate(board):
            if num in line:
                array[i][j][line.index(num)] = 'x'


def get_winner(array):
    for i, board in enumerate(array):
        cols_dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
        }
        for line in board:
            if 'x' not in line:
                continue

            marks_in_line = 0
            for j, el in enumerate(line):
                if el == 'x':
                    marks_in_line += 1
                    cols_dict[j + 1] += 1

            if marks_in_line == 5:
                return array.pop(i)

        if 5 in cols_dict.values():
            return array.pop(i)
    return None


def second_part(array):
    all_result = get_all_winners(array)
    winner_num, winner = all_result[-1]

    sum_unchecked = 0
    for line in winner:
        for el in line:
            if el != 'x':
                sum_unchecked += int(el)

    print(winner_num * sum_unchecked)


first_part(deepcopy(input_array))
second_part(deepcopy(input_array))
