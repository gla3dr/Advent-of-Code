with open('2017/Day5/input.txt', 'r') as f:
    pc = 0
    steps = 0
    instructions = [int(l) for l in f]
    while pc < len(instructions):
        temp = pc
        inst = instructions[pc]
        pc += inst
        instructions[temp] += 1
        steps += 1
    print steps
