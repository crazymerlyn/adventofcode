from src.machine import Machine
from src.coord import *

def part1(lines):
    n = 50
    inputs = [(i, j) for i in range(n) for j in range(n)]
    res = 0
    grid = {}

    ops = [int(x) for x in lines[0].strip().split(',')]

    for y, x in inputs:
        machine = Machine(ops, [x, y])
        grid[x + y*1j] = next(machine.run())
        res += grid[x + y*1j]
    print(pretty_grid(grid, mapper=lambda x: " X"[x]))
    return res

def part2(lines):
    ops = [int(x) for x in lines[0].strip().split(',')]

    def get_val(x, y):
        return next(Machine(ops, [x, y]).run())

    valids = [[y for y in range(20) if get_val(x, y)] for x in range(10)]
    lo = min(valids[9])
    right_limit = 1000

    for x in range(10, right_limit):
        while not get_val(x, lo): lo += 1

        if x < 99: continue
        if get_val(x-99, lo+99):
            return (x-99) * 10000 + lo
