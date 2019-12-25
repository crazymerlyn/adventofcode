from src.machine import Machine

def part1(lines):
    opcodes = [int(x) for x in lines[0].strip().split(',')]
    m = Machine(opcodes, [ord(x) for x in "inv\n"])
    while True:
        out = []
        for x in m.run():
            if x is None: break
            out.append(chr(x))
        print("".join(out))
        m.input = [ord(x) for x in input()] + [10]
