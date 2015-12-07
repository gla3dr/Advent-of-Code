from collections import defaultdict
funcs = {
    'SIG' : (lambda in1, in2: in1),
    'AND' : (lambda in1, in2: in1 & in2),
    'OR' : (lambda in1, in2: in1 | in2),
    'NOT' : (lambda in1, in2: ~ in1),
    'LSHIFT' : (lambda in1, in2: in1 << in2),
    'RSHIFT' : (lambda in1, in2: in1 >> in2)
}

wires = defaultdict(int) 

def get_operand(op):
    try:
        return int(op)
    except ValueError:
        return wires[op]

with open('test_input.txt') as input:
    for line in input:
        parts = line.split()
        operand1 = None
        operand2 = None
        operator = None
        result = None
        if len(parts) == 3:
            operand1 = get_operand(parts[0])
            operator = 'SIG'
        elif len(parts) == 4:
            operand1 = get_operand(parts[1])
            operator = parts[0]
        elif len(parts) == 5:
            operand1 = get_operand(parts[0])
            operand2 = get_operand(parts[2])
            operator = parts[1]
        result = parts[-1]
        wires[result] = funcs[operator](operand1, operand2)
print wires
