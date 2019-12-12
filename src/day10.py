import math
from math import gcd
from collections import defaultdict

def key(a, b):
  g = gcd(a, b)
  return (a // g, b // g)

def angle(x, y):
  ang = math.atan2(y, -x)
  return ang + 2*math.pi if ang < 0 else ang

def dist(a, b, a2, b2):
  return abs(a - a2) + abs(b - b2)

def get_laser_pos(mat):
  n = len(mat)
  m = len(mat[0])

  data = [[defaultdict(list) for _ in range(m)] for _ in range(n)]

  for i in range(n):
    for j in range(m):
      if mat[i][j] == '.': continue
      for i2 in range(n):
        for j2 in range(m):
          if i == i2 and j == j2: continue
          if mat[i2][j2] == '.': continue
          data[i][j][key(i2-i, j2-j)].append((i2, j2))

  best = max([(i, j) for i in range(n) for j in range(m)], key=lambda x: len(data[x[0]][x[1]]))
  return best, data

def part1(lines):
  mat = [line.strip() for line in lines]

  (i, j), data = get_laser_pos(mat)
  return len(data[i][j])

def part2(lines):
  mat = [line.strip() for line in lines]

  (i, j), data = get_laser_pos(mat)
  data = data[i][j]

  for k in data:
    data[k] = sorted(data[k], key=lambda x: dist(i, j, x[0], x[1]))

  destroyed = 0
  while True:
    for k in sorted(data.keys(), key=lambda x: angle(*x)):
      if not data[k]: continue
      i, j = data[k].pop(0)
      destroyed += 1

      if destroyed == 200:
        return j * 100 + i
    break

if __name__ == '__main__':
  import sys
  lines = sys.stdin.readlines()
  print(part1(lines[:]))
  print(part2(lines[:]))
