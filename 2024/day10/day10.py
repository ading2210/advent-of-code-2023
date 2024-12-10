import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")
topography = [[int(h) for h in line] for line in lines]

trailheads = []
for y, row in enumerate(topography):
  for x, height in enumerate(row):
    if height == 0:
      trailheads.append((y, x))

offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))

def walk_trail(trail):
  y, x, curr_height = trail[-1]
  found_trails = []
  if curr_height == 9:
    found_trails.append(trail)
    return found_trails

  for offset_x, offset_y in offsets:
    new_x, new_y = x + offset_x, y + offset_y
    if new_x < 0 or new_x >= len(topography[y]):
      continue
    if new_y < 0 or new_y >= len(topography):
      continue
    
    new_height = topography[new_y][new_x]
    if new_height == curr_height + 1:
      new_trail = trail + [(new_y, new_x, new_height)]
      found_trails += walk_trail(new_trail)

  return found_trails

trail_count = 0
trail_ratings = 0 
for y, x in trailheads:
  trails = walk_trail([(y, x, 0)])
  trail_ends = set([trail[-1] for trail in trails])
  trail_count += len(trail_ends)
  trail_ratings += len(trails)

print(trail_count, trail_ratings)