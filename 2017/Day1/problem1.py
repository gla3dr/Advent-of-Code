from itertools import izip, islice
with open('2017/Day1/input.txt', 'r') as f:
    for l in f:
        total = sum([int(c) for c, n in izip(l, islice(l, 1, None)) if int(c) == int(n) ])
        total = total + int(l[-1]) if int(l[-1]) == int(l[0]) else total
        print(total)
