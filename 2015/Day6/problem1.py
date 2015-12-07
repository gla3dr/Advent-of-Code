lights = set()
with open('input.txt') as input:
    for inst in input:
        parts = inst.split()
        if parts[0] == 'turn':
            start = parts[2].split(',')
            end = parts[4].split(',')
            for x in range(int(start[0]), int(end[0])+1):
                for y in range(int(start[1]), int(end[1])+1):
                    if parts[1] == 'on':
                        lights.add((x,y))
                    elif parts[1] == 'off':
                        lights.discard((x,y))
        elif parts[0] == 'toggle':
            start = parts[1].split(',')
            end = parts[3].split(',')
            for x in range(int(start[0]), int(end[0])+1):
                for y in range(int(start[1]), int(end[1])+1):
                    if (x,y) in lights:
                        lights.remove((x,y))
                    else:
                        lights.add((x,y))
    print len(lights)
