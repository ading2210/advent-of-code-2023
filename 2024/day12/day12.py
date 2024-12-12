import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")
garden = [list(line) for line in lines]
offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))

#use the flood fill algorithm to determine regions
def find_region(region, x, y, plant):
  region.append((x, y))

  for offset_x, offset_y in offsets:
    new_x = x + offset_x
    new_y = y + offset_y

    if new_y < 0 or new_y >= len(garden):
      continue
    if new_x < 0 or new_x >= len(garden[new_y]):
      continue
    if (new_x, new_y) in region:
      continue

    tile = garden[new_y][new_x]
    if tile != plant:
      continue

    find_region(region, new_x, new_y, plant)
  
  return region

#find all regions by looking for a region at each point in the garden
def find_regions():
  regions = []
  for y, row in enumerate(garden):
    for x, tile in enumerate(row):
      for region in regions:
        if (x, y) in region:
          break
      else:
        region = find_region([], x, y, tile)
        regions.append(region)
  return regions

#find every point in a region where its neighbors are also in the same region
def find_border(region):
  border = []
  perimeter = 0
  for x, y in region:
    for offset_x, offset_y in offsets:
      new_x = x + offset_x
      new_y = y + offset_y

      if (new_x, new_y) in region:
        continue
      perimeter += 1
      border.append((x, y, new_x, new_y))

  return perimeter, border

#walk along a side of a border and get all the points in the side
def walk_side(side, border, pos): 
  x, y, outer_x, outer_y = pos
  offset_x_abs = abs(outer_y - y)
  offset_y_abs = abs(outer_x - x)
  offsets = ((offset_x_abs, offset_y_abs), (-offset_x_abs, -offset_y_abs))

  side.append(pos)

  for offset_x, offset_y in offsets:
    new_x = x + offset_x
    new_y = y + offset_y
    new_outer_x = outer_x + offset_x
    new_outer_y = outer_y + offset_y
    new_pos = (new_x, new_y, new_outer_x, new_outer_y)
    if new_pos in side:
      continue
    if not new_pos in border:
      continue
    walk_side(side, border, new_pos)
  
  return side

#count number of sides in a region's border
def find_sides(border):
  sides = []
  for pos in border:
    for side in sides:
      if pos in side:
        break
    else:
      side = walk_side([], border, pos)
      sides.append(side)
  return sides

#calculate price of each region
regular_price = 0
bulk_price = 0
regions = find_regions()
for region in regions:
  perimeter, border = find_border(region)
  area = len(region)
  regular_price += area * perimeter

  sides = find_sides(border)
  side_count = len(sides)
  bulk_price += area * side_count
  
print(regular_price, bulk_price)