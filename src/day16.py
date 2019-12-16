#!/usr/bin/python3
import numpy as np

def single_digit(digits, i):
    result = 0
    for j in range(0, len(digits), 4*i):
        result += sum(digits[j+i-1:j+2*i-1]) - sum(digits[j+3*i-1:j+4*i-1])
    return abs(result) % 10

def part1(lines):
    digits = [int(x) for x in lines[0].strip()]

    for i in range(100):
        digits = [single_digit(digits, i) for i in range(1, len(digits) + 1)]
    return "".join(map(str, digits[:8]))

def part2(lines):
    digits = [int(x) for x in lines[0].strip()] * 10000
    offset = int("".join(map(str, digits[:7])))
    digits = np.array(digits[offset:][::-1])

    for i in range(100):
        digits = digits.cumsum() % 10
    return "".join(map(str, digits[-8:][::-1]))

