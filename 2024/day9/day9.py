import pathlib
import itertools

disk_map = pathlib.Path("data.txt").read_text()
file_sizes = [int(x) for x in disk_map[::2]]
free_spaces = [int(x) for x in disk_map[1::2]]

disk = []
files = []

zipped = itertools.zip_longest(file_sizes, free_spaces, fillvalue=0)
for id, (file_size, free_space) in enumerate(zipped):
  for j in range(file_size):
    disk.append(id)
  for j in range(free_space):
    disk.append(None)
  if file_size:
    files.append([id, file_size])
  if free_space:
    files.append([None, free_space])

p1_disk = disk[:]
p2_disk = []

def checksum(blocks):
  total = 0
  for i, block in enumerate(blocks):
    if block is None:
      continue
    total += i * block
  return total

#rearrange by blocks for part 1
while None in p1_disk:
  last = p1_disk.pop(-1)
  if last is None:
    continue
  space_index = p1_disk.index(None)
  p1_disk[space_index] = last

print(checksum(p1_disk))

def find_space(desired_size):
  for i, (id, size) in enumerate(files):
    if not id is None:
      continue
    if size >= desired_size:
      return i, (id, size)
  return None, None

def find_file(desired_id):
  for i, (id, size) in enumerate(files):
    if id == desired_id:
      return i, (id, size)
  return None, None

#rearrange by whole files for part 2
for id in reversed(range(len(file_sizes))):
  f_index, file = find_file(id)
  s_index, space = find_space(file[1])

  if space is None:
    continue
  if s_index > f_index:
    continue
  files[s_index][1] = space[1] - file[1]
  files[f_index][0] = None
  files.insert(s_index, file)

for id, size in files:
  for i in range(size):
    p2_disk.append(id)

#print(p2_disk)
print(checksum(p2_disk))