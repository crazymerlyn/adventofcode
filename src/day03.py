step = {'R':1, 'L': -1, 'U': 1j, 'D':-1j}

def points(line):
  dirs = line.strip().split(',')
  steps = [(step[d[0]], int(d[1:])) for d in dirs]
  cur = 0
  res = []
  for dt, dist in steps:
    for _ in range(dist):
      cur += dt
      res.append(cur)
  return res

def part1(lines):
  wire1 = points(lines[0])
  wire2 = points(lines[1])

  return int(min(abs(x.real) + abs(x.imag) for x in set(wire1) & set(wire2)))

def part2(lines):
  wire1 = points(lines[0])
  wire2 = points(lines[1])

  dist1 = {p: i + 1 for i, p in enumerate(wire1)}
  dist2 = {p: i + 1 for i, p in enumerate(wire2)}

  return min(dist1[p] + dist2[p] for p in dist1 if p in dist2)
