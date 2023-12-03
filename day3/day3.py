import re
import pathlib

#this code sucks - way too many nested loops lol

lines = pathlib.Path("data.txt").read_text().split("\n")

def is_symbol(char):
  return char != "." and not char.isdigit()

def get_partnums_1():
  for i, line in enumerate(lines):
    num_regex = r'\d+'

    for match in re.finditer(num_regex, line):
      startindex = match.start(0) - 1
      endindex = match.end(0)
      number = int(match.group(0))
      yield i, line, startindex, endindex, number
    
def part1():
  total = 0

  for i, line, startindex, endindex, number in get_partnums_1():
    if startindex >= 0 and is_symbol(line[startindex]):
      total += number
      continue
    elif endindex < len(line) and is_symbol(line[endindex]):
      total += number
      continue

    for j in range(startindex, endindex+1):
      if j >= len(line):
        continue
      if i > 0 and is_symbol(lines[i-1][j]):
        total += number
        break
      elif i < len(lines)-2 and is_symbol(lines[i+1][j]):
        total += number
        break
  
  print(total)

def get_partnums_2():
  parts = []
  for i, line in enumerate(lines):
    num_regex = r'\d+'
    parts.append([])

    for match in re.finditer(num_regex, line):
      startindex = match.start(0)
      endindex = match.end(0) - 1
      number = int(match.group(0))
      part = (startindex, endindex, number)
      parts[i].append(part)
  
  return parts

def part2():
  total = 0
  parts = get_partnums_2()

  for i, line in enumerate(lines):
    for j, char in enumerate(line):
      if char != "*":
        continue

      adjacent_parts = []
      for k in range(-1, 2):
        if i+k < 0 or i+k > len(lines):
          continue
        for startindex, endindex, number in parts[i+k]:
          if startindex-1 <= j <= endindex+1:
            adjacent_parts.append(number)
      
      if len(adjacent_parts) == 2:
        total += adjacent_parts[0] * adjacent_parts[1]
  
  print(total)

part2()