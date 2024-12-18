import pathlib
import math

maze = pathlib.Path("data.txt").read_text().split("\n")
offsets = ((1, 0), (0, -1), (-1, 0), (0, 1))

for y, row in enumerate(maze):
  for x, tile in enumerate(row):
    if tile == "S":
      start_x, start_y = x, y
    elif tile == "E":
      end_x, end_y = x, y

def find_neighbors(x, y, direction, nodes, reverse=False):
  offset_x, offset_y = direction
  new_x, new_y = x + offset_x, y + offset_y
  if reverse:
    new_x, new_y = x - offset_x, y - offset_y

  #move forward 1 tile
  neighbors = []
  if maze[new_y][new_x] != "#" and (new_x, new_y, direction) in nodes:
    neighbors.append(nodes[(new_x, new_y, direction)])

  #turn 90 degrees in place
  new_directions = ((offset_y, offset_x), (-offset_y, -offset_x))
  for new_direction in new_directions:
    if (x, y, new_direction) in nodes:
      neighbors.append(nodes[((x, y, new_direction))])
  return neighbors

#use dijkstra's algorithm to find all paths to the ending
#return the visited nodes and the shortest distance
def find_path_dijkstra():
  unvisited = {}
  visited = {}
  min_distance = 0
  end_node = None

  for y, row in enumerate(maze):
    for x, tile in enumerate(row):
      if tile == "#":
        continue
      for direction in offsets:
        offset_x, offset_y = direction
        new_x, new_y = x + offset_x, y + offset_y
        #store the distance, position, and direction as a node
        unvisited[(x, y, direction)] = [math.inf, x, y, direction]
  
  #add the starting node
  unvisited[(start_x, start_y, (1, 0))] = [0, start_x, start_y, (1, 0)]
  
  while unvisited:
    node_key = min(unvisited, key=lambda x: unvisited[x][0])
    current_node = unvisited.pop(node_key)
    visited[node_key] = current_node

    distance, x, y, direction = current_node
    if distance == math.inf:
      break
    if (x, y) == (end_x, end_y) and min_distance == 0:
      min_distance = distance
      end_node = current_node

    neighbors = find_neighbors(x, y, direction, unvisited)
    for neighbor in neighbors:
      new_distance = distance
      old_distance, new_x, new_y, new_direction = neighbor
      if new_direction != direction:
        new_distance += 1000
      if (new_x, new_y) != (x, y):
        new_distance += 1
      neighbor[0] = min(old_distance, new_distance)
  
  return min_distance, visited, end_node

#use a depth first search to walk backwards though the visited nodes from dijkstra's algorithm
def walk_shortest_paths(nodes, visited, node):
  distance, x, y, direction = node
  visited.append(node)
  neighbors = find_neighbors(x, y, direction, nodes, reverse=True)
  for neighbor in neighbors:
    new_distance = neighbor[0]
    if new_distance < distance:
      walk_shortest_paths(nodes, visited, neighbor)
  return visited

distance, nodes, end_node = find_path_dijkstra()
print(distance)

path_nodes = walk_shortest_paths(nodes, [], end_node)
path_tiles = set([(x, y) for distance, x, y, direction in path_nodes])
print(len(path_tiles))
