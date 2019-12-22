def parse_shuffle(lines, deck_size):
    mul = 1
    add = 0

    for line in lines:
        line = line.strip()
        if line == "deal into new stack":
            mul *= -1
            add = add * -1 + deck_size - 1
        elif line.startswith("cut"):
            n = int(line.split()[1])
            add -= n
        elif line.startswith("deal with increment"):
            n = int(line.split()[-1])
            mul = mul * n % deck_size
            add = add * n % deck_size
        else:
            raise RuntimeError("Unknown command: " % line)
    return mul, add

def repeat_mul(mul, add, times, mod):
    return pow(mul, times, mod), add * (pow(mul, times, mod) - 1) * pow(mul-1, mod-2, mod) % mod

def part1(lines):
    deck_size = 10007
    mul, add = parse_shuffle(lines, deck_size)
    return (2019 * mul + add) % deck_size

def part2(lines):
    deck_size = 119315717514047
    times = 101741582076661

    final = 2020
    mul, add = parse_shuffle(lines, deck_size)
    mul, add = repeat_mul(mul, add, times, deck_size)

    # final = x * mul + add
    x = (final - add) * pow(mul, deck_size-2, deck_size) % deck_size
    return x

