with open('2017/Day1/input.txt', 'r') as f:
    for l in f:
        total = 0
        full = len(l)
        half = full/2
        for i, c in enumerate(l):
            nexthalf = int(l[(i + half) % full])
            total = total + int(c) if int(c) == nexthalf else total
        print total
