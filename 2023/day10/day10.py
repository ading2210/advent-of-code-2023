import re
import pathlib

#i can't be bothered to write this algorithm myself
#https://stackoverflow.com/a/23453678
import matplotlib.path as mplPath
import numpy as np

lines = pathlib.Path("data.txt").read_text().split("\n")
pipe_offsets = {
  "|": ((0, 1), (0, -1)),
  "-": ((1, 0), (-1, 0)),
  "L": ((0, -1), (1, 0)),
  "J": ((0, -1), (-1, 0)),
  "7": ((0, 1), (-1, 0)),
  "F": ((0, 1), (1, 0)),
  ".": (),
  "S": ((0, 1), (0, -1), (1, 0), (-1, 0)), 
}

def find_connections(x, y):
  pipe = lines[y][x]
  offsets = pipe_offsets[pipe]

  connections = []
  for offset_x, offset_y in offsets:
    new_x = x + offset_x
    new_y = y + offset_y

    if not 0 <= new_y < len(lines):
      continue
    if not 0 <= new_x < len(lines[0]):
      continue

    pipe2 = lines[new_y][new_x]
    offsets2 = pipe_offsets[pipe2]

    for offset_x2, offset_y2 in offsets2:
      new_x2 = new_x + offset_x2
      new_y2 = new_y + offset_y2

      if new_x2 == x and new_y2 == y:
        connections.append((new_x, new_y))
        break
  
  return connections

#this takes 3 seconds for some reason but still gives the right answer
def part1():
  for i, line in enumerate(lines):
    if "S" in line:
      start_x = line.index("S")
      start_y = i
      break
  
  last_visited = find_connections(start_x, start_y)
  all_visited = [(start_x, start_y)] + last_visited
  steps = 1

  while True:
    just_visited = []
    for x, y in last_visited:
      connections = find_connections(x, y)
      valid_connections = [pos for pos in connections if not pos in all_visited]
      just_visited += valid_connections
      all_visited += valid_connections

    if just_visited == []:
      print(steps)
      return
    
    steps += 1
    last_visited = just_visited

def part2():
  for i, line in enumerate(lines):
    if "S" in line:
      start_x = line.index("S")
      start_y = i
      break
  
  last_pipe = (start_x, start_y)
  current_pipe = find_connections(*last_pipe)[0]
  start_pipe = current_pipe

  loop = []
  while True:
    next_connections = find_connections(*current_pipe)
    for pipe in next_connections:
      if pipe != last_pipe:
        next_pipe = pipe
        break
    
    loop.append(next_pipe)
    if next_pipe == start_pipe:
      break

    last_pipe = current_pipe
    current_pipe = next_pipe

  loop_array = np.array(loop)
  loop_path = mplPath.Path(loop_array)

  total = 0
  for y, line in enumerate(lines):
    for x, tile in enumerate(line):
      point = (x, y)
      if point in loop:
        continue
      if loop_path.contains_point(point):
        total += 1

  print(total)

part2()