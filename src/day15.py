#!/usr/bin/python3

from collections import defaultdict, Counter
from fractions import Fraction
from fractions import gcd
from src.machine import Machine
from src.coord import *

def children(node, state):
    return [node + x for x in [1, -1, 1j, -1j]]

def find_dir(pos, state):
    q = [pos]
    parent = {pos: None}
    while q:
        node = q.pop(0)
        if node not in state:
            while parent[node] != pos:
                node = parent[node]
            return node - pos
        for child in children(node, state):
            if child in state and state[child] == '#': continue
            if child in parent: continue
            q.append(child)
            parent[child] = node

def max_dist(state, a):
    q = [a]
    dist = {a: 0}
    while q:
        node = q.pop(0)
        for child in children(node, state):
            if child in dist: continue
            if state[child] == '#': continue
            dist[child] = dist[node] + 1
            q.append(child)
    return max(dist.values())

def get_dist(state, a, b):
    q = [a]
    dist = {a: 0}
    while q:
        node = q.pop(0)
        if node == b:
            return dist[b]
        for child in children(node, state):
            if child in dist: continue
            if state[child] == '#': continue
            dist[child] = dist[node] + 1
            q.append(child)

def explore(lines):
    dir2code = {1: 4, -1: 3, 1j: 1, -1j: 2}
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    pos = 0
    opos = 0

    state = defaultdict(lambda: '?')
    state[pos] = 'D'
    last_dir = 1
    directions = [dir2code[last_dir]]

    m = Machine(opcodes, directions)
    for out in m.run():
        if out == 0:
            state[pos + last_dir] = '#'
        elif out == 1:
            state[pos] = '.'
            pos += last_dir
            state[pos] = 'D'
        elif out == 2:
            state[pos] = '.'
            pos += last_dir
            state[pos] = 'O'
            opos = pos
        else:
            print("unknown", out)
        last_dir = find_dir(pos, state)
        if last_dir is None:
            return state, opos
        directions.append(dir2code[last_dir])

def part1(lines):
    state, opos = explore(lines)
    return get_dist(state, 0, opos)

def part2(lines):
    state, opos = explore(lines)
    return max_dist(state, opos)

