import re
import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

def extrapolate(history):
  diffs = [history]

  for i in range(len(history)-1):
    diffs.append([])
    prev_diff = diffs[i]
    new_diff = diffs[i+1]

    for value, next_value in zip(prev_diff, prev_diff[1:]):
      new_diff.append(next_value - value)

    if new_diff.count(0) == len(new_diff):
      break

  diffs.reverse()
  result = 0
  
  for i, diff in enumerate(diffs):
    if i == 0: continue
    prev_diff = diffs[i-1]
    diff.append(diff[-1] + prev_diff[-1])

  return diffs[-1][-1]


def part1(reverse=False):
  total = 0
  for line in lines:
    history = [int(s) for s in line.split()]
    if reverse:
      history.reverse()
    next_value = extrapolate(history)
    total += next_value
  
  print(total)

def part2():
  part1(reverse=True)

part1()
part2()