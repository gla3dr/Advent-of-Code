lights = [[0 for x in range(1000)] for y in range(1000)]
with open('input.txt') as input:
    for inst in input:
        parts = inst.split()
        if parts[0] == 'turn':
            start = parts[2].split(',')
            end = parts[4].split(',')
            for x in range(int(start[0]), int(end[0])+1):
                for y in range(int(start[1]), int(end[1])+1):
                    if parts[1] == 'on':
                        lights[x][y] += 1
                    elif parts[1] == 'off':
                        lights[x][y] = max(lights[x][y]-1, 0)
        elif parts[0] == 'toggle':
            start = parts[1].split(',')
            end = parts[3].split(',')
            for x in range(int(start[0]), int(end[0])+1):
                for y in range(int(start[1]), int(end[1])+1):
                    lights[x][y] += 2
    print(sum(map(sum, lights)))
