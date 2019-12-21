#!/usr/bin/python3
from heapq import *

def mapper(row):
    res = []
    for c in row:
        if c.isalpha():
            if c.lower() == c:
                res.append(1 << (ord(c) - ord('a')))
            else:
                res.append(-(1 << (ord(c) - ord('A'))))
        elif c == '#': res.append(-(1 << 27))
        elif c == '@': res.append('@')
        else: res.append(0)
    return res

def start_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@': return (i, j)

def get_dist(grid, a):
    n = len(grid)
    m = len(grid[0])
    grid[a[0]][a[1]] = 0
    key_count = sum(1 for row in grid for c in row if c > 0)
    final = (1 << key_count) - 1

    q = [(a, 0)]
    dist = {(a, 0): 0}

    def children(node, keys):
        i, j = node
        for i2, j2 in [(i+1, j), (i,j+1), (i,j-1), (i-1,j)]:
            if i2 < 0 or i2 >= n or j2 < 0 or j2 >= m: continue
            if grid[i2][j2] < 0 and (keys & -grid[i2][j2] == 0): continue
            if grid[i2][j2]>0:
                yield (i2, j2), keys | grid[i2][j2]
            else:
                yield (i2, j2), keys

    i = 0
    while q:
        node, keys = q.pop(0)
        if i % 10000 == 0:
            print(i, bin(keys))
        i += 1
        if keys == final: return dist[(node, keys)]
        for child in children(node, keys):
            if child in dist: continue
            dist[child] = dist[(node, keys)] + 1
            q.append(child)
    return(dist)

def part1(lines):
    grid = [mapper(x) for x in lines]
    return get_dist(grid, start_pos(grid))

def part2(lines):
    return None


if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    print(part1(lines))
    print(part2(lines))
