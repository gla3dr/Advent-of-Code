with open('input.txt') as input:
    for line in input:
        delivered = 1
        x = 0
        y = 0
        houses = [(0,0)]
        for c in line:
            if c == '>':
                x += 1
            elif c == '<':
                x -= 1
            elif c == '^':
                y += 1
            elif c == 'v':
                y -= 1
            
            coords = (x,y)
            if not coords in houses:
                delivered += 1
                houses.append(coords)
        
        print(delivered)