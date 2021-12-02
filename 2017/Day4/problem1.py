with open('2017/Day4/input.txt', 'r') as f:
  print(len([l for l in f if len(set(l.split())) == len(l.split())]))