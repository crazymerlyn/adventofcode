from collections import defaultdict

def get_graph(lines):
    parent = {}
    graph = defaultdict(list)
    for line in lines:
        u, v  = line.strip().split(')')
        parent[v] = u
        graph[u].append(v)

    depth = {"COM": 0}
    q = ["COM"]
    while q:
        node = q.pop(0)
        for child in graph[node]:
            depth[child] = depth[node] + 1
            q.append(child)

    return parent, depth

def part1(lines):
    parent, depth = get_graph(lines)
    return sum(depth.values())

def part2(lines):
    parent, depth = get_graph(lines)
    a = parent["YOU"]
    b = parent["SAN"]

    res = 0
    while a != b:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
        res += 1
    return res
