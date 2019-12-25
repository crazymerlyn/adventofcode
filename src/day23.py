from src.machine import Machine

def part1(lines):
    ops = [int(x) for x in lines[0].strip().split(',')]
    machines = [Machine(ops[:], [i]) for i in range(50)]
    run= [True] * len(machines)
    while True:
        for i, machine in enumerate(machines):
            runner = machine.run()
            while True:
                dest = next(runner)
                if dest is None:
                    machine.input = [-1]*10
                    break
                x = next(runner)
                y = next(runner)
                if dest == 255:
                    return y
                machines[dest].input.extend([x, y])

def remove_ones(x):
    while len(x) and x[0] == -1: x.pop(0)

def part2(lines):
    ops = [int(x) for x in lines[0].strip().split(',')]
    machines = [Machine(ops[:], [i]) for i in range(50)]
    run= [True] * len(machines)
    prevlast = None
    last = []
    while True:
        anyoutput = False
        for i, machine in enumerate(machines):
            runner = machine.run()
            while True:
                dest = next(runner)
                if dest is None:
                    machine.input = [-1]
                    break
                anyoutput = True
                x = next(runner)
                y = next(runner)
                if dest == 255:
                    last = [x, y]
                else:
                    remove_ones(machines[dest].input)
                    machines[dest].input.extend([x, y])
        if not anyoutput:
            if prevlast == last:
                return last[1]
            machines[0].input = last[:]
            prevlast = last
