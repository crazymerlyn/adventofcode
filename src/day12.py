import re
from math import gcd

def lcm(a, b):
    return a*b//gcd(a,b)

def parse(line):
    return [[int(x) for x in re.findall('[-\d]+', line)], [0, 0, 0]]

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def energy(moons):
    return sum(sum(map(abs, x)) * sum(map(abs,v)) for x, v in moons)

def next_step(moons):
    for dimension in range(3):
        for x1, v1 in moons:
            for x2, v2 in moons:
                v1[dimension] += sign(x2[dimension] - x1[dimension])
        for x1, v1 in moons:
            x1[dimension] += v1[dimension]
    return moons

def iterate(moons, steps):
    for _ in range(steps):
        moons = next_step(moons)
    return moons

def simple_next_step(moons):
    for m1 in moons:
        for m2 in moons:
            m1[1] += sign(m2[0] - m1[0])
    for m1 in moons:
        m1[0] += m1[1]
    return moons

def iterate_til_repeat(moons, dimension):
    moons = [[x[dimension], v[dimension]] for x, v in moons]
    orig = [[x,v] for x,v in moons]
    i = 1
    moons = simple_next_step(moons)
    while moons != orig:
        moons = simple_next_step(moons)
        i += 1
    return i

def part1(lines):
    moons = [parse(line) for line in lines]

    moons = iterate(moons, 1000)

    return energy(moons)

def part2(lines):
    moons = [parse(line) for line in lines]
    res = 1
    for dim in range(3):
        res = lcm(res, iterate_til_repeat(moons[:], dim))
    return res
