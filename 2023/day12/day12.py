import pathlib
import functools

lines = pathlib.Path("data.txt").read_text().split("\n")

@functools.cache
def find_combinations(springs, sizes, group_size=0):
  if not springs:
    if len(sizes) == 1 and sizes[0] == group_size:
      return 1
    if not sizes and not group_size:
      return 1
    return 0

  combinations = 0

  branches = springs[0]
  if branches == "?":
    branches = "#."

  for char in branches:
    if char == "#":
      combinations += find_combinations(springs[1:], sizes, group_size+1)
    elif group_size:
      if sizes and sizes[0] == group_size:
        combinations += find_combinations(springs[1:], sizes[1:])
    else:
      combinations += find_combinations(springs[1:], sizes)
  
  return combinations


def all_arrangements(part2=False):
  total = 0
  for line in lines:
    springs, sizes_str = line.split()
    sizes = tuple(int(s) for s in sizes_str.split(","))

    if part2:
      springs = "?".join([springs] * 5)
      sizes = sizes * 5

    total += find_combinations(springs, sizes)
    
  return total

def part1():
  print(all_arrangements())

def part2():
  print(all_arrangements(True))

part2()