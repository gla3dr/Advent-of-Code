with open('2021/Day1/input1.txt', 'r') as i:
    input = [int(d) for d in i.readlines()]

    # sums = [sum(w) for w in zip(input, input[1:], input[2:])]
    print(len([(a,b) for (a,b) in zip([sum(w) for w in zip(input, input[1:], input[2:])], [sum(w) for w in zip(input, input[1:], input[2:])][1:]) if b>a]))