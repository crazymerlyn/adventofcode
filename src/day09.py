from src.machine import Machine

def part1(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')] + [0] * 3000
    return next(Machine(opcodes, [1]).run())

def part2(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')] + [0] * 3000
    return next(Machine(opcodes, [2]).run())
