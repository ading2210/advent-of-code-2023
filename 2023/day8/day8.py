import re
import pathlib
import math

lines = pathlib.Path("data.txt").read_text().split("\n")
instructions = lines[0]
node_lines = lines[2:]

def parse_nodes():
  nodes = {}
  for node_str in node_lines:
    node_regex = r'(...) = \((...), (...)\)'
    node_id, left_node, right_node = re.findall(node_regex, node_str)[0]
    nodes[node_id] = (left_node, right_node)
  return nodes

def num_steps(nodes, start_node, part2=True):
  current_node = start_node
  steps = 0
  
  while True:
    for instruction in instructions:
      node = nodes[current_node]
      if instruction == "L":
        current_node = node[0]
      else:
        current_node = node[1]

      steps += 1
      if part2 and current_node[2] == "Z":
        return steps
      if not part2 and current_node == "ZZZ":
        return steps

def part1():
  nodes = parse_nodes()
  
  steps = num_steps(nodes, "AAA", False)
  print(steps)

def part2():
  nodes = parse_nodes()
  
  start_nodes = [node_id for node_id in nodes if node_id[2] == "A"]
  step_counts = [num_steps(nodes, node_id) for node_id in start_nodes]
  final_steps = math.lcm(*step_counts)

  print(final_steps)

part1()
part2()