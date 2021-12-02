with open('input.txt', 'r') as f:
    total = 0
    for line in f:
      dims = [ int(x) for x in line.split('x') ]
      sides = []
      sides.append(dims[0]*dims[1])
      sides.append(dims[0]*dims[2])
      sides.append(dims[1]*dims[2])
      small = min(sides)
      total += (2*sides[0]) + (2*sides[1]) + (2*sides[2]) + small
    
    print(total)
      