funcs = {
    'SIG' : (lambda in1, in2: in1),
    'AND' : (lambda in1, in2: in1 & in2),
    'OR' : (lambda in1, in2: in1 | in2),
    'NOT' : (lambda in1, in2: ~ in1),
    'LSHIFT' : (lambda in1, in2: in1 << in2),
    'RSHIFT' : (lambda in1, in2: in1 >> in2)
}

wires = {} 

def solve(operation):
    v1 = None
    v2 = None
    try:
        v1 = int(operation[0])
    except ValueError:
        v1 = int(solve(wires[operation[0]]))
        wires[operation[0]] = (v1, 'SIG', None)
    if operation[2] is not None:
        try:
            v2 = int(operation[2])
        except ValueError:
            v2 = int(solve(wires[operation[2]]))
            wires[operation[2]] = (v2, 'SIG', None)
    return funcs[operation[1]](v1, v2)


with open('input.txt') as input:
    for line in input:
        parts = line.split()
        operand1 = None
        operand2 = None
        operator = None
        result = parts[-1]
        if len(parts) == 3:
            operand1 = parts[0]
            operator = 'SIG'
        elif len(parts) == 4:
            operand1 = parts[1]
            operator = parts[0]
        elif len(parts) == 5:
            operand1 = parts[0]
            operand2 = parts[2]
            operator = parts[1]
        wires[result] = (operand1, operator, operand2)
print solve(wires['a'])
