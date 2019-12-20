from collections import defaultdict
from heapq import *

def recursive_labelify(grid):
    n = len(grid)
    m = len(grid[0])

    def is_outer(i, j):
        return i == 2 or i == n - 3 or j == 2 or j == m - 3

    for i in range(n):
        for j in range(m):
            if not grid[i][j].isupper(): continue
            for i2, j2 in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if i2 < 0 or i2 >= n or j2 < 0 or j2 >= m: continue
                if grid[i2][j2].isupper() and len(grid[i2][j2]) == 1:
                    if (i2 < i or (i2 == i and j2 < j)):
                        (i, j), (i2, j2) = (i2, j2), (i, j)
                    val = "".join([grid[i][j], grid[i2][j2]])
                    grid[i][j] = val
                    grid[i2][j2] = val

    portal = defaultdict(list)
    graph = defaultdict(list)
    graph2 = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.': continue
            for i2, j2 in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if i2 < 0 or i2 >= n or j2 < 0 or j2 >= m: continue
                if grid[i2][j2] == '.':
                    graph[(i, j)].append((i2, j2))
                elif grid[i2][j2].isupper():
                    portal[grid[i2][j2]].append((i, j))

    start = None
    end = None
    for key, vals in portal.items():
        if len(vals) == 1:
            if key == 'AA': start = vals[0][0], vals[0][1], 0
            else:
                end = vals[0][0], vals[0][1], 0
            continue
        assert len(vals) == 2, (key, vals)
        if is_outer(*vals[0]):
            vals[0], vals[1] = vals[1], vals[0]
        elif is_outer(*vals[1]):
            pass
        else:
            assert False
        graph2[vals[0]].append((vals[1][0], vals[1][1], 1))
        graph2[vals[1]].append((vals[0][0], vals[0][1], -1))
    return graph, graph2, start, end

def labelify(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if not grid[i][j].isupper(): continue
            for i2, j2 in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if i2 < 0 or i2 >= n or j2 < 0 or j2 >= m: continue
                if grid[i2][j2].isupper() and len(grid[i2][j2]) == 1:
                    if (i2 < i or (i2 == i and j2 < j)):
                        (i, j), (i2, j2) = (i2, j2), (i, j)
                    val = "".join([grid[i][j], grid[i2][j2]])
                    grid[i][j] = val
                    grid[i2][j2] = val

    portal = defaultdict(list)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.': continue
            for i2, j2 in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if i2 < 0 or i2 >= n or j2 < 0 or j2 >= m: continue
                if grid[i2][j2] == '.':
                    graph[(i, j)].append((i2, j2))
                elif grid[i2][j2].isupper():
                    portal[grid[i2][j2]].append((i, j))

    start = None
    end = None
    for key, vals in portal.items():
        if len(vals) == 1:
            if key == 'AA': start = vals[0]
            else:
                end = vals[0]
            continue
        assert len(vals) == 2
        graph[vals[0]].append(vals[1])
        graph[vals[1]].append(vals[0])
    return graph, start, end

def get_dist(graph, start, end):
    q = [start]
    dist = {start: 0}
    while q:
        node = q.pop(0)
        for child in graph[node]:
            if child in dist: continue
            dist[child] = dist[node] + 1
            q.append(child)
    return dist[end]

def get_dist2(graph, graph2, start, end):
    start = start[:2]
    end = end[:2]
    q = [(0, start)]
    dist = {(0, start): 0}
    maxlevel = 10000
    i = 0
    while q:
        i += 1
        level, node = heappop(q)
        if node == end and level == 0:
            return dist[(level, node)]
        for child in graph[node[:2]]:
            child = child[0], child[1]
            if (level, child) in dist: continue
            dist[(level, child)] = dist[(level, node)] + 1
            heappush(q, (level, child))
        for child in graph2[node[:2]]:
            newlevel = level + child[2]
            if newlevel < 0 : continue
            if newlevel > 127: continue
            child = child[0], child[1]
            if (newlevel,child) in dist: continue
            dist[(newlevel,child)] = dist[(level,node)] + 1
            heappush(q, (newlevel, child))
    return dist[(0, end)]

def part1(lines):
    grid = [list(line.strip('\n')) for line in lines]
    graph, start, end = labelify(grid)
    return get_dist(graph, start, end)


def part2(lines):
    grid = [list(line.strip('\n')) for line in lines]
    graph, graph2, start, end = recursive_labelify(grid)
    return get_dist2(graph, graph2, start, end)

if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    print(part1(lines))
    print(part2(lines))
