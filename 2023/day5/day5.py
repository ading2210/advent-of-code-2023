import re
import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

class Rule:
  def __init__(self, dest, src, length):
    self.dest = dest
    self.dest_end = dest + length
    self.src = src
    self.src_end = src + length
    self.length = length
    self.offset = src - dest

  def __repr__(self):
    return f'Rule(dest={self.dest}, src={self.src}, length={self.length})'
  
def parse_map(map_str):
  rules = []
  nums_regex = r'(\d+) (\d+) (\d+)'
  for nums in re.findall(nums_regex, map_str):
    rule_args = list(map(int, nums))
    rules.append(Rule(*rule_args))
  
  return rules

def convert_num(map_, number, reverse=False):
  for rule in map_:
    src, dest = rule.src, rule.dest
    if reverse:
      src, dest = dest, src

    if src <= number < src + rule.length:
      return dest + number - src
    
  return number

def walk_maps(maps, number, reverse=False):
  if reverse:
    maps = maps[::-1]
  
  result = number
  for map_ in maps:
    result = convert_num(map_, result, reverse=reverse)
  
  return result

def part1():
  seeds = [int(s) for s in lines[0][6:].split()]
  map_lines = lines[2:]
  map_strs = "\n".join(map_lines).split("\n\n")
  
  maps = [parse_map(map_str) for map_str in map_strs]
  locations = []

  for seed in seeds:
    location = walk_maps(maps, seed)
    locations.append(location)
  
  print(min(locations))

def part2():
  seed_nums = [int(s) for s in lines[0][6:].split()]
  seed_ranges = list(zip(seed_nums[::2], seed_nums[1::2]))

  map_strs = "\n".join(lines[2:]).split("\n\n")
  maps = [parse_map(map_str) for map_str in map_strs]

  seeds = [a[0] for a in seed_ranges]
  seeds += [a[0] + a[1] for a in seed_ranges]
  
  for i, map_ in enumerate(maps):
    new_values = []
    for rule in map_:
      new_values += [rule.src, rule.src_end-1]
    
    previous_maps = maps[:i]
    for new_value in new_values:
      new_seed = walk_maps(previous_maps, new_value, reverse=True)
      seeds.append(new_seed)
  
  filtered_seeds = []
  for seed in seeds:
    for seed_start, seed_count in seed_ranges:
      if seed_start <= seed < seed_start + seed_count:
        filtered_seeds.append(seed)
      
  locations = []
  for seed in filtered_seeds:
    location = walk_maps(maps, seed)
    locations.append(location)
    
  print(min(locations))

part1()
part2()