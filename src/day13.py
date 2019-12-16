#!/usr/bin/python3

from collections import defaultdict, Counter
from fractions import Fraction
from fractions import gcd
import sys
from math import atan2, pi
from src.machine import Machine
from src.coord import *

def lcm(*args):
    res = args[0]
    for a in args[1:]:
        res = res * a // gcd(res, a)
    return res

def pretty(x):
    if x == 0: return '.'
    if x == 1: return '#'
    if x == 2: return '%'
    if x == 3: return '-'
    return 'O'


def part1(lines):
    res = 0
    grid = [[0] * 100 for _ in range(100)]
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    mach = Machine(opcodes, []).run()
    try:
        while True:
            i = next(mach)
            j = next(mach)
            x = next(mach)
            grid[j][i] = x
    except StopIteration:
        pass

    for line in grid:
        #print("".join(map(pretty, line)))
        res  += sum(1 for x in line if x == 2)
    return res

def part2(lines):
    def get_input():
        if ball_pos[1] > paddle_pos[1]: return 1
        elif ball_pos[1] < paddle_pos[1]: return -1
        return 0
    grid = [[0] * 100 for _ in range(100)]
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    opcodes[0] = 2
    mach = Machine(opcodes, get_input).run()
    score = 0
    ball_pos = 0, 0
    paddle_pos = 0, 0
    try:
        while True:
            i = next(mach)
            j = next(mach)
            x = next(mach)
            if i == -1 and j == 0:
                score = x
                continue
            grid[j][i] = x
            if x == 4: ball_pos = j, i
            elif x == 3: paddle_pos = j, i
    except StopIteration:
        return score
