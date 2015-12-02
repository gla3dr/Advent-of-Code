floor = 0
index = 0
with open('aoc1in.txt') as f:
	for line in f:
		for c in line:
			index += 1
			if c == '(':
				floor += 1
			elif c == ')':
				floor -= 1
			if floor < 0:
				print index
				exit()
