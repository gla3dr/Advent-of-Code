import json
encodes = 0
literals = 0
with open('input.txt') as input:
    for line in input:
        line = line.replace('\n', '')
        literals += len(line)
        encoded = json.dumps(line)
        encodes += len(encoded)
print(encodes - literals)
