from src import machine

def part1(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    m = machine.Machine(opcodes, [1])

    return list(m.run())[-1]

def part2(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    m = machine.Machine(opcodes, [5])

    return list(m.run())[-1]
