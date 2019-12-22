import functools
def part1(lines):
    total = 10007
    deck = list(range(total))
    for line in lines:
        line = line.strip()
        if line == "deal into new stack":
            deck = deck[::-1]
        elif line.startswith("cut"):
            n = int(line.split()[1])
            if n < 0: n += total
            deck = deck[n:] + deck[:n]
        elif line.startswith("deal with increment"):
            n = int(line.split()[-1])
            newdeck = deck[:]
            for i in range(total):
                x = n * i % total
                newdeck[x] = deck[i]
            deck = newdeck
        else:
            print(line)
    return deck.index(2019)


def part2(lines):
    total = 119315717514047
    times = 101741582076661

    @functools.lru_cache(500)
    def inv(n):
        return pow(n, total-2, total)

    idx = 2020
    seen = set([idx])
    mul = 1
    add = 0
    for line in lines[::-1]:
        line = line.strip()
        if line == "deal into new stack":
            mul *= -1
            add = add * -1 + total - 1
        elif line.startswith("cut"):
            n = int(line.split()[1])
            if n < 0: n += total
            add += n
        elif line.startswith("deal with increment"):
            n = int(line.split()[-1])
            mul = mul * inv(n) % total
            add = add * inv(n) % total
        else:
            print(line)
    idx = idx * pow(mul, times, total) + add * (pow(mul, times, total) - 1) * pow(mul-1, total - 2, total)
    return idx % total

