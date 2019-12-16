#!/usr/bin/python3

from collections import defaultdict, Counter
from fractions import Fraction
from fractions import gcd
from math import ceil
import sys
from math import atan2, pi
from src.machine import Machine
from src.coord import *


def make_graph(lines):
    cost = {}
    parent = defaultdict(list)
    zeroes = ["FUEL"]
    children = defaultdict(int)
    for line in lines:
        i, o = line.strip().split(" => ")
        i = [x.strip().split() for x in i.split(",")]
        for x in i: x[0] = int(x[0])
        co, o = o.strip().split(" ")
        co = int(co)
        cost[o] = [(x[1], x[0], co) for x in i]
        for _, name in i:
            children[name] += 1
            parent[o].append(name)
    top = []
    while zeroes:
        node = zeroes.pop(0)
        top.append(node)
        for p in parent[node]:
            children[p] -= 1
            if children[p] == 0:
                zeroes.append(p)
    return cost, top

def ore_needed(val, cost, top):
    res = 0
    need = defaultdict(int)
    need["FUEL"] = val

    for name in top:
        q = need[name]
        if name == "ORE": return q
        for child, need1, get1 in cost[name]:
            need[child] += need1 * ceil(q/get1)

def part1(lines):
    cost, top = make_graph(lines)
    return ore_needed(1, cost, top)

def part2(lines):
    cost, top = make_graph(lines)
    lo = 1
    high = 10 ** 12
    while lo != high:
        mid = (lo + high + 1) // 2
        res = ore_needed(mid, cost, top)
        if res <= 1000000000000:
            lo = mid
        else:
            high = mid - 1

    return lo
