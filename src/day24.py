def parse(lines):
    res = []
    for line in lines:
        line = line.strip()
        res.append(line)
    return tuple(res)

def step(x):
    newx = [list(y) for y in x]
    for i in range(5):
        for j in range(5):
            count = 0
            for i2, j2 in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if i2 < 0 or i2 >= 5 or j2 < 0 or j2 >= 5: continue
                if x[i2][j2] == '#': count += 1
            if (x[i][j] == '#' and count == 1) or (x[i][j] != '#' and count in (1,2)):
                newx[i][j] = '#'
            else:
                newx[i][j] = '.'
    return tuple("".join(row) for row in newx)

def adj(k, i, j):
    if i == 0:
        yield k - 1, 1, 2
    elif i == 3 and j == 2:
        for j2 in range(5):
            yield k+1, 4, j2
    else:
        yield k, i-1, j

    if j == 0:
        yield k - 1, 2, 1
    elif j == 3 and i == 2:
        for i2 in range(5):
            yield k+1, i2, 4
    else:
        yield k, i, j-1

    if i == 4:
        yield k - 1, 3, 2
    elif i == 1 and j == 2:
        for j2 in range(5):
            yield k+1, 0, j2
    else:
        yield k, i+1, j

    if j == 4:
        yield k - 1, 2, 3
    elif j == 1 and i == 2:
        for i2 in range(5):
            yield k+1, i2, 0
    else:
        yield k, i, j+1


def newstep(xs):
    newxs = [[list(y) for y in x] for x in xs]
    for k in range(1, len(newxs)-1):
        for i in range(5):
            for j in range(5):
                count = 0
                if i == 2 and j == 2:
                    newxs[k][i][j] = '?'
                    continue
                for k2, i2, j2 in adj(k, i, j):
                    count += xs[k2][i2][j2] == '#'
                if (xs[k][i][j] == '#' and count == 1) or (xs[k][i][j] == '.' and count in (1,2)):
                    newxs[k][i][j] = '#'
                else:
                    newxs[k][i][j] = '.'
    return newxs

def diversity(x):
    res = 0
    for i in range(5):
        for j in range(5):
            if x[i][j] == '#':
                res += 2 ** (i * 5 + j)
    return res

def part1(lines):
    x = parse(lines)
    seen = set()
    while x not in seen:
        seen.add(x)
        x = step(x)
    return diversity(x)

def get_bugs(xs):
    res = 0
    for x in xs:
        for row in x:
            res += row.count("#")
    return res

def pretty_print(xs):
    for x in xs:
        for row in x:
            print("".join(row))
        print()

def part2(lines):
    x = [list(line) for line in parse(lines)]
    xs = [['.'*5 for _ in range(5)] for _ in range(201)]
    xs = xs + [x] + xs
    for _ in range(200):
        xs = newstep(xs)
    return get_bugs(xs)

if __name__ == '__main__':
    import sys
    lines = sys.stdin.readlines()
    print(part1(lines))
    print(part2(lines))
