import itertools

with open("2017/Day2/input.txt") as f:
    print sum(itertools.chain.from_iterable([[int(i)/int(j) for i in l.split("\t") for j in l.split("\t") if int(i) % int(j) == 0 and i != j] for l in f]))