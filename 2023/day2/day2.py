import re
import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")
colors = ["red", "green", "blue"]

def part1():
  total = 0
  for i, line in enumerate(lines):
    item_regex = r'(\d+) (blue|red|green)'
    matches = re.findall(item_regex, line)
    invalid = False

    for count, color in matches:
      if int(count) > colors.index(color) + 12:
        invalid = True
        break
  
    if not invalid:
      total += i + 1
  
  print(total)

def part2():
  total = 0
  for i, line in enumerate(lines):
    item_regex = r'(\d+) (blue|red|green)'
    matches = re.findall(item_regex, line)

    min_cubes = [0, 0, 0]
    for count, color in matches:
      index = colors.index(color)
      min_cubes[index] = max(min_cubes[index], int(count))
    total += min_cubes[0] * min_cubes[1] * min_cubes[2]
  
  print(total)

part2()