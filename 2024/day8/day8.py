import pathlib
import itertools

lines = pathlib.Path("data.txt").read_text().split("\n")

antennas = {}
antinodes = set()

for y, line in enumerate(lines):
  for x, char in enumerate(line):
    if char == ".":
      continue
    if char in antennas:
      antennas[char].append((x, y))
    else:
      antennas[char] = [(x, y)]

for frequency, coords in antennas.items():
  combinations = itertools.combinations(coords, 2)

  for (x1, y1), (x2, y2) in combinations:
    diff_x = x1 - x2
    diff_y = y1 - y2

    new_x1, new_y1 = x1 + diff_x, y1 + diff_y
    new_x2, new_y2 = x2 - diff_x, y2 - diff_y
    
    antinodes.add((new_x1, new_y1))
    antinodes.add((new_x2, new_y2))

lines_new = [list(line) for line in lines]
total = 0
for x, y in antinodes:
  if x < 0 or x >= len(lines[0]):
    continue
  if y < 0 or y >= len(lines):
    continue
  lines_new[y][x] = "#"
  total += 1

for line in lines_new:
  print("".join(line))

print(total)