with open('2021/Day1/input1.txt', 'r') as i:
    input = [int(d) for d in i.readlines()]

    print(len([(x, y) for (x, y) in zip(input, input[1:]) if y > x]))
