import re
import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

def vertical_expansion(image, part2):
  for i in range(len(image)-1, -1, -1):
    line = image[i]
    if not "#" in line:
      image.insert(i, "!"*len(line))
  return image

def expand_all(image, part2=False):
  image = vertical_expansion(image, part2)
  image = list(zip(*image[::-1])) #rotate the 2d array clockwise
  image = vertical_expansion(image, part2) #horizontal expansion
  image = list(zip(*image))[::-1] #rotate it back
  return ["".join(line) for line in image] #convert back to strings

def get_galaxies(image):
  galaxies = []
  for y, line in enumerate(image):
    for x, char in enumerate(line):
      if char != "#": continue
      galaxies.append((x, y))
  return galaxies

def get_distance(image, galaxy1, galaxy2, multiplier):
  start_x = min(galaxy1[0], galaxy2[0])
  start_y = min(galaxy1[1], galaxy2[1])
  end_x = max(galaxy1[0], galaxy2[0])
  end_y = max(galaxy1[1], galaxy2[1])

  row = image[start_y][start_x:end_x]
  x_distance = end_x - start_x
  x_distance += max(multiplier - 2, 0) * row.count("!")

  col = "".join([line[start_x] for line in image])[start_y:end_y]
  y_distance = end_y - start_y
  y_distance += max(multiplier - 2, 0) * col.count("!")
  
  return x_distance + y_distance
      
def all_distances(multiplier):
  image = expand_all(lines[:])
  galaxies = get_galaxies(image)
  
  total = 0
  for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
      total += get_distance(image, galaxy1, galaxy2, multiplier)

  return total

def part1():
  print(all_distances(1))

def part2():
  print(all_distances(1_000_000))

part1()
part2()