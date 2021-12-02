floor = 0
with open('aoc1in.txt') as f:
	for line in f:
		for c in line:
			if c == '(':
				floor += 1
			elif c == ')':
				floor -= 1
	print(floor)
