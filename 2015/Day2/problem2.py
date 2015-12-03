with open('input.txt', 'r') as f:
    total = 0
    for line in f:
      dims = [ int(x) for x in line.split('x') ]
      bow = reduce(lambda x, y: x*y, dims)
      small = min(dims)
      dims.remove(small)
      med = min(dims)
      ribbon = 2*small + 2*med
      total += ribbon + bow
    print total