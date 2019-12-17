#!/usr/bin/python3
from src.machine import Machine

def explore(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    m = Machine(opcodes, [])
    l = list(m.run())
    return "".join(map(chr, l)).strip().split("\n")

def part1(lines):
    grid = explore(lines)
    n = len(grid)
    m = len(grid[0])
    res = 0
    for i in range(n):
        for j in range(m):
            if not grid[i][j] in '#<>^v': continue
            count = 0
            if j > 0 and grid[i][j-1] in '#><^v':
                count += 1
            if i > 0 and grid[i-1][j] in '#><^v':
                count += 1
            if j < m - 1 and grid[i][j+1] in '#><^v':
                count += 1
            if i < n - 1 and grid[i+1][j] in '#><^v':
                count += 1
            if count > 2:
                res += i * j
    return res

def part2(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    opcodes[0] = 2

    directions = 'A,B,A,C,B,C,A,B,A,C\nR,10,L,8,R,10,R,4\nL,6,L,6,R,10\nL,6,R,12,R,12,R,10\nn\n'
    directions = [ord(x) for x in directions]

    m = Machine(opcodes, directions)
    l = list(m.run())
    print("".join(map(chr, l[:-1])))
    return l[-1]

