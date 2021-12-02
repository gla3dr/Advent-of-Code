with open('2017/Day4/input.txt', 'r') as f:
  print(len([l for l in f if len(set([''.join(sorted(w)) for w in l.split()])) == len([''.join(sorted(w)) for w in l.split()])]))