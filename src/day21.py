from src.machine import Machine
from src.coord import *

def part1(lines):
    ops = [int(x) for x in lines[0].strip().split(',')]
    commands = ["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "NOT D T", "NOT T T", "AND T J", "WALK"]
    machine = Machine(ops, list(ord(x) for x in "\n".join(commands) + "\n"))
    res = 0

    out = [chr(x) if x < 127 else str(x) for x in machine.run()]
    return "".join(out)

def part2(lines):
    ops = [int(x) for x in lines[0].strip().split(',')]
    commands = ["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "NOT D T", "NOT T T", "AND T J", "NOT I T", "NOT T T", "OR F T", "AND E T", "OR H T", "AND T J", "RUN"]
    machine = Machine(ops, list(ord(x) for x in "\n".join(commands) + "\n"))
    res = 0

    out = [chr(x) if x < 127 else str(x) for x in machine.run()]
    return "".join(out)
