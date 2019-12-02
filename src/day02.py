def run_machine(opcode):
    i = 0
    while opcode[i] != 99:
        if opcode[i] == 1:
            opcode[opcode[i + 3]] = opcode[opcode[i + 1]] + opcode[opcode[i + 2]]
        elif opcode[i] == 2:
            opcode[opcode[i + 3]] = opcode[opcode[i + 1]] * opcode[opcode[i + 2]]
        else:
            raise RuntimeError("Invalid opcode: %d", opcode[i])
        i += 4
    return opcode[0]

def part1(lines):
    opcode = [int(x) for x in lines[0].strip().split(",")]

    opcode[1] = 12
    opcode[2] = 2

    return run_machine(opcode)


def part2(lines):
    opcodes = [int(x) for x in lines[0].strip().split(",")]

    for noun in range(1, 100):
        for verb in range(1, 100):
            opcode = opcodes[:]
            opcode[1] = noun
            opcode[2] = verb
            try:
                result = run_machine(opcode)
            except:
                continue
            if result == 19690720:
                return 100 * noun + verb
