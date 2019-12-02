def fuel(x):
    return max(x // 3 - 2, 0)

def total_fuel(x):
    return 0 if x <= 6 else fuel(x) + total_fuel(fuel(x))

def part1(lines):
    return sum(fuel(int(line)) for line in lines)

def part2(lines):
    return sum(total_fuel(int(line)) for line in lines)
