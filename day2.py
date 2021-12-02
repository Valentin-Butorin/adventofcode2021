with open('day2_input.txt') as f:
    array = list(map(lambda x: x.split(' '), f.read().split('\n')))

x = 0
y = 0

for direction, step in array:
    if direction == 'forward':
        x += int(step)
    if direction == 'up':
        y -= int(step)
    if direction == 'down':
        y += int(step)

print(x * y)

aim = 0
x = 0
y = 0

for direction, step in array:
    if direction == 'forward':
        x += int(step)
        if aim > 0:
            y += aim * int(step)
    if direction == 'up':
        aim -= int(step)
    if direction == 'down':
        aim += int(step)

print(x * y)
