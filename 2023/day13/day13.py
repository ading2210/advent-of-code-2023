import pathlib

pattern_strs = pathlib.Path("data.txt").read_text().split("\n\n")
patterns = [s.split("\n") for s in pattern_strs]

def horizontal_reflection(pattern):
  valid = set()
  for i, row in enumerate(pattern):
    reflection_size = min(i, len(pattern)-i)
    before = pattern[i-reflection_size:i]
    after = pattern[i:i+reflection_size][::-1]

    if before == after and reflection_size:
      valid.add(i)

  return valid

def vertical_reflection(pattern):
  rotated_pattern = list(zip(*pattern[::-1]))
  return horizontal_reflection(rotated_pattern)

def part1():
  total = 0
  for pattern in patterns:
    horizontal = horizontal_reflection(pattern) or {0}
    vertical = vertical_reflection(pattern) or {0}

    total += 100 * min(horizontal) + min(vertical)
  
  print(total)

def edit_pattern(pattern, x, y):
  new_pattern = [list(row) for row in pattern]
  if new_pattern[y][x] == ".":
    new_pattern[y][x] = "#"
  else:
    new_pattern[y][x] = "."
  edited_pattern = ["".join(row) for row in new_pattern]
  return edited_pattern

#this is wayyy longer than it needs to be but it works somehow
def find_new_line(pattern):
  horizontal = horizontal_reflection(pattern)
  vertical = vertical_reflection(pattern)

  for y in range(len(pattern)):
    for x in range(len(pattern[y])):
      edited_pattern = edit_pattern(pattern, x, y)
      new_horizontal = horizontal_reflection(edited_pattern)
      new_vertical = vertical_reflection(edited_pattern)

      if not new_horizontal and not new_vertical:
        continue
      different_horizontal = new_horizontal - horizontal
      different_vertical = new_vertical - vertical

      if not different_horizontal and not different_vertical:
        continue
      return different_horizontal, different_vertical
  
  return set(), set()

def part2():
  total = 0
  for pattern in patterns:
    new_line = find_new_line(pattern)
    horizontal = new_line[0] or {0}
    vertical = new_line[1] or {0}
    total += 100 * min(horizontal) + min(vertical)

  print(total)

part1()
part2()