with open('2021/Day1/input1.txt', 'r') as i:
    input = [int(d) for d in i.readlines()]

    # sums = [sum(w) for w in zip(input, input[1:], input[2:])]
    print(len([(a,b) for (a,b) in zip([sum(w) for w in zip(input, input[1:], input[2:])], [sum(w) for w in zip(input, input[1:], input[2:])][1:]) if b>a]))

    # After realizing that (a+b+c < b+c+d) == (a < d) the solution becomes much simpler...
    print(len([(x, y) for (x, y) in zip(input, input[3:]) if y > x]))
