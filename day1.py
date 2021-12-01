with open('day1_input.txt') as f:
    array = list(map(lambda x: int(x), f.read().split('\n')))

i = 0
result_cnt = 0
while i < len(array) - 1:
    if array[i] < array[i + 1]:
        result_cnt += 1
    i += 1

print(result_cnt)

result_cnt = 0
prev_sum = sum(array[0:3])
i = 1
while i < len(array) - 2:
    current_sum = sum(array[i:i + 3])
    if current_sum > prev_sum:
        result_cnt += 1
    prev_sum = current_sum
    i += 1

print(result_cnt)
