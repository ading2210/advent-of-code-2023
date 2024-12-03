import pathlib
import re

data = pathlib.Path("data.txt").read_text()
mul_regex = r"mul\((\d+),(\d+)\)"
matches = re.findall(mul_regex, data)
result = sum([int(a) * int(b) for a, b in matches])

new_regex = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
enabled = True
new_total = 0
for a, b, do, dont in re.findall(new_regex, data):
  if do:
    enabled = True
  elif dont:
    enabled = False
  elif enabled:
    new_total += int(a) * int(b)

print(result, new_total)