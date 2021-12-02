import re
with open('2021/Day2/input.txt', 'r') as i:
    commands =  i.read()
    print(
        sum([int(f) for f in re.findall(r'forward (\d)', commands)])
        *
        (
            sum([int(d) for d in re.findall(r'down (\d)', commands)])
            -
            sum([int(u) for u in re.findall(r'up (\d)', commands)])
        )
    )
