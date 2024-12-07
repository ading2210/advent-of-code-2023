import pathlib
import math
import re

lines = pathlib.Path("data.txt").read_text().split("\n")
board = [list(line) for line in lines]

#find starting pos
for start_y, row in enumerate(board):
  if not "^" in row:
    continue
  start_x = row.index("^")
  break

def run_guard(return_visited=False):
  x, y = start_x, start_y
  angle = 0.5
  visited_set = set()
  while True:
    if (x, y, angle) in visited_set:
      return True
    else:
      visited_set.add((x, y, angle))
    new_x = x + round(math.cos(angle * math.pi))
    new_y = y - round(math.sin(angle * math.pi))
    if new_x < 0 or new_y < 0:
      break
    if new_y >= len(board) or new_x >= len(board[new_y]):
      break

    if board[new_y][new_x] == "#":
      angle -= 0.5
      angle %= 2
    else:
      x, y = new_x, new_y

  return visited_set if return_visited else False

visited = run_guard(True)
visited_coords = set([(x, y) for x, y, angle in visited])
visited_total = len(visited_coords)

loops_found = 0
iterations = 0
for x, y in visited_coords:
  iterations += 1
  char = board[y][x]
  if char == "#" or char == "^":
    continue
  board[y][x] = "#"
  loops_found += 1 if run_guard() else 0
  board[y][x] = char

print(visited_total, loops_found)