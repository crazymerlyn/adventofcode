def isvalid1(x):
    double = any(str(i) * 2 in x for i in range(10))
    return double and sorted(str(x)) == list(str(x))

def isvalid2(x):
    double = any(str(i) * 2 in x and str(i) * 3 not in x for i in range(10))
    return double and sorted(str(x)) == list(str(x))

def countvalid(start, end, valid):
    res = 0
    for i in range(start, end+1):
        res += valid(str(i))
    return res

def part1(lines):
    a, b = [int(x) for x in lines[0].strip().split('-')]
    return countvalid(a, b, isvalid1)

def part2(lines):
    a, b = [int(x) for x in lines[0].strip().split('-')]
    return countvalid(a, b, isvalid2)

