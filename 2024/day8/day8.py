import pathlib
import itertools

lines = pathlib.Path("data.txt").read_text().split("\n")

antennas = {}

for y, line in enumerate(lines):
  for x, char in enumerate(line):
    if char == ".":
      continue
    if char in antennas:
      antennas[char].append((x, y))
    else:
      antennas[char] = [(x, y)]

def add_antinode(x, y):
  if x < 0 or x >= len(lines[0]):
    return False
  if y < 0 or y >= len(lines):
    return False
  antinodes.add((x, y))
  return True

def add_line(x, y, diff_x, diff_y, part2=False):
  while True:
    x += diff_x
    y += diff_y
    in_bounds = add_antinode(x, y)
    if not in_bounds or not part2:
      break

def make_antinodes(part2=False):
  for frequency, coords in antennas.items():
    pairs = itertools.combinations(coords, 2)

    for (x1, y1), (x2, y2) in pairs:
      diff_x = x1 - x2
      diff_y = y1 - y2

      if part2:
        add_antinode(x1, y1)
        add_antinode(x2, y2)
        
      add_line(x1, y1, diff_x, diff_y, part2)
      add_line(x2, y2, -diff_x, -diff_y, part2)

antinodes = set()
make_antinodes()
print(len(antinodes))

antinodes = set()
make_antinodes(True)
print(len(antinodes))