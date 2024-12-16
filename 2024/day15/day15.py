import pathlib
import itertools

warehouse_str, movements_str = pathlib.Path("data.txt").read_text().split("\n\n")
movements = movements_str.replace("\n", "")

offsets = {
  "^": (0, -1),
  "v": (0, 1),
  ">": (1, 0),
  "<": (-1, 0)
}

class Warehouse:
  def __init__(self, warehouse):
    self.board = []
    self.boxes = []
    self.robot_x = 0
    self.robot_y = 0

    for y, row in enumerate(warehouse):
      self.board.append([])
      for x, tile in enumerate(row):
        self.board[y].append("#" if tile == "#" else ".")
        if tile == "@":
          self.robot_x = x
          self.robot_y = y
        elif tile == "O":
          self.boxes.append([[x, y]])
        elif tile == "[":
          self.boxes.append([[x, y], [x + 1, y]])
  
  def find_box(self, x, y):
    for box in self.boxes:
      for box_x, box_y in box:
        if box_x == x and box_y == y:
          return box
    return None
  
  def find_box_chain(self, box, offset_x, offset_y):
    found_boxes = [box]
    for box_x, box_y in box:
      next_box = self.find_box(box_x + offset_x, box_y + offset_y)
      if not next_box:
        continue
      if next_box in found_boxes:
        continue
      found_boxes.extend(self.find_box_chain(next_box, offset_x, offset_y))
    return found_boxes

  def push_boxes(self, x, y, offset_x, offset_y):
    next_box = self.find_box(x + offset_x, y + offset_y)
    box_coords = [[x, y]]
    box_chain = []

    if next_box:
      box_chain_tmp = self.find_box_chain(next_box, offset_x, offset_y)
      for box in box_chain_tmp:
        if not box in box_chain:
          box_chain.append(box)
      box_coords.extend(itertools.chain(*box_chain))
    
    for box_x, box_y in box_coords:
      next_tile = self.board[box_y + offset_y][box_x + offset_x]
      if next_tile == "#":
        return False

    for box in box_chain:
      for box_pos in box:
        box_pos[0] += offset_x
        box_pos[1] += offset_y
    
    return True
  
  def run_robot(self, movements):
    for direction in movements:
      offset_x, offset_y = offsets[direction]
      move_success = self.push_boxes(self.robot_x, self.robot_y, offset_x, offset_y)
      if move_success:
        self.robot_x += offset_x
        self.robot_y += offset_y
    
    return sum((box[0][0] + box[0][1]*100 for box in self.boxes))

warehouse_1 = Warehouse(warehouse_str.split("\n"))
print(warehouse_1.run_robot(movements))

warehouse_str_2 = warehouse_str.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
warehouse_2 = Warehouse(warehouse_str_2.split("\n"))
print(warehouse_2.run_robot(movements))