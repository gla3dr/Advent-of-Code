with open('2021/Day2/input.txt', 'r') as i:
    aim = 0
    depth = 0
    horiz = 0
    for c in i.readlines():
        c, v = c.split(' ')
        if c == 'up':
            aim -= int(v)
        elif c == 'down':
            aim += int(v)
        elif c == 'forward':
            horiz += int(v)
            depth += int(v) * aim
    print(depth * horiz)
