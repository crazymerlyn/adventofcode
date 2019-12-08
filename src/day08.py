from collections import Counter
n=25
m=6

def bit(x):
    if x == '1': return '\u25CF'
    return  ' '

def part1(lines):
    data = lines[0].strip()
    layers = [data[i:i+n*m] for i in range(0,len(data),n*m)]
    layer = min(layers, key=lambda l: Counter(l)['0'])
    c = Counter(layer)
    return c['1'] * c['2']

def part2(lines):
    data = lines[0].strip()
    layers = [data[i:i+n*m] for i in range(0,len(data),n*m)]
    ans = ['2' for _ in layers[0]]
    for layer in layers:
        for i, x in enumerate(layer):
            if ans[i] == '2':
                ans[i] = x
    return "\n".join("".join(bit(x) for x in ans[i:i+n]) for i in range(0, n*m, n))

