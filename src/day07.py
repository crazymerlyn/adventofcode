from src import machine
import itertools

def part1(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')]

    max_val = 0
    for perm in itertools.permutations(range(5)):
        val = 0
        for phase in perm:
            m = machine.Machine(opcodes[:], [phase, val])
            val = next(m.run())
        max_val = max(val, max_val)

    return max_val

def part2(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    max_val = 0
    for perm in itertools.permutations(range(5, 10)):
        inputs = [[phase] for phase in perm]
        inputs[0].append(0)
        machines = [machine.Machine(opcodes[:], inputs[i]).run() for i in range(5)]
        while True:
            try:
                for i in range(5):
                    inputs[(i + 1) % 5].append(next(machines[i]))
            except StopIteration:
                max_val = max(inputs[0][-1], max_val)
                break

    return max_val

    return list(m.run())[-1]

