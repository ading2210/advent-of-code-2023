import pathlib
import re
import math

lines = pathlib.Path("data.txt").read_text().split("\n")

iterations = 100
width = 101
height = 103
robots = []

#example input only
#width = 11
#height = 7

for line in lines:
  matches = re.findall(r"[-\d]+", line)
  x, y, vx, vy = [int(i) for i in matches]
  robots.append([x, y, vx, vy])

quadrants = [0, 0, 0, 0]

for x, y, vx, vy in robots:
  x = (x + vx * iterations) % width
  y = (y + vy * iterations) % height

  mid_x = width//2
  mid_y = height//2
  if x < mid_x and y < mid_y:
    quadrants[0] += 1
  elif x < mid_x and y > mid_y:
    quadrants[1] += 1
  elif x > mid_x and y < mid_y:
    quadrants[2] += 1
  elif x > mid_x and y > mid_y:
    quadrants[3] += 1

safety_factor = math.prod(quadrants)
print(safety_factor)

pictures = 0
for i in range(1, 100000):
  new_robots = []
  board = [[0 for j in range(width)] for j in range(height)]
  for x, y, vx, vy in robots:
    x = (x + vx * i) % width
    y = (y + vy * i) % height
    new_robots.append((x, y))
    board[y][x] = 1

  if len(set(new_robots)) != len(new_robots):
    continue
  
  max_sum = max((sum(row) for row in board))
  #the tree picture has 31 robots in a single row 
  if max_sum > 30:
    print(i)
    break

