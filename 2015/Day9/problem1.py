edges = []
mst = []
parents = {}
sets = {}

def union(edge):
    p1 = parents[edge[0]]
    p2 = parents[edge[1]]
    if p1 in sets and p2 in sets:
        for v in sets[p2]:
            parents[v] = p1
        sets[p1] = sets[p1].union(sets[p2])
        sets.pop(p2)
    elif p1 in sets:
        sets[p1].add(edge[1])
        parents[edge[1]] = p1
    elif p2 in sets:
        sets[p2].add(edge[0])
        parents[edge[0]] = p2
    else:
        sets[p1] = set()
        sets[p1].add(edge[0])
        sets[p1].add(edge[1])
        parents[edge[1]] = p1

with open('test_input.txt') as graph:
    for line in graph:
        parts = line.split()
        edges.append((parts[0], parts[2], int(parts[4])))
        parents[parts[0]] = parts[0]
        if parts[2] not in parents:
            parents[parts[2]] = parts[2]
edges.sort(key=lambda tup: tup[2])
print(edges)
for edge in edges:
    if parents[edge[0]] != parents[edge[1]]:
        print("Add edge: {}".format(edge))
        mst.append(edge)
        union(edge)
        print("Sets: {}".format(sets))
        print("Parents: {}\n".format(parents))
print(sum([e[2] for e in mst]))
