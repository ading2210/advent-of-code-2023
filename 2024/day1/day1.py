import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")
lines_split = [line.split("   ") for line in lines]
left, right = list(map(list, zip(*lines_split))) #transpose

left = sorted([int(l) for l in left])
right = sorted([int(r) for r in right])

part_1 = sum([abs(l - r) for l, r in zip(left,right)])
part_2 = sum([l * right.count(l) for l, r in zip(left,right)])

print(part_1, part_2)