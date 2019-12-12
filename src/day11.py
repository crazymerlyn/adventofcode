from src.machine import Machine
from src.coord import *
from collections import defaultdict

def get_final_state(lines, initial_state=0):
  opcodes = [int(x) for x in lines[0].strip().split(',')]
  m = Machine(opcodes, [])
  runner = m.run()
  pos = 0
  dt = 1j
  state = defaultdict(int)
  state[pos] = initial_state

  try:
    while True:
      m.input = [state[pos]]
      state[pos] = next(runner)

      dt = [left, right][next(runner)](dt)
      pos += dt
  except StopIteration:
    pass

  return state

def part1(lines):
  return len(get_final_state(lines))

def part2(lines):
  return pretty_grid(get_final_state(lines,1), mapper=lambda x: '#' if x else '.')

if __name__ == '__main__':
  import sys
  lines = sys.stdin.readlines()
  print(part1(lines))
  print(part2(lines))
