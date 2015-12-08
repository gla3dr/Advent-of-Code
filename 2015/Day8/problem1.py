literals = 0
escapes = 0
with open('input.txt') as input:
    for line in input:
        literals += len(line)
        escaped = line[1:-1].decode('string_escape')
        escapes += len(escaped)
print literals - escapes
