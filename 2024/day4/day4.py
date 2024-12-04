import pathlib
import re

#this is a regex-based solution which is obviously not very good

lines = pathlib.Path("data.txt").read_text().split("\n")

xmas_regex = r"(?=(XMAS|SAMX))"

def find_count(board):
  return len(re.findall(xmas_regex, "\n".join(board)))

def transpose(board):
  return ["".join(i) for i in zip(*board)]

def shift_diagonal(board):
  return ["."*i + line + "."*(len(board)-1-i) for i, line in enumerate(board)]

total = find_count(lines)
total += find_count(transpose(lines))
total += find_count(transpose(shift_diagonal(lines)))
total += find_count(transpose(shift_diagonal(list(reversed(lines)))))

#part 2
new_regex = [r"M.S", r".A.", r"M.S"]
new_regex_reverse = [line[::-1] for line in new_regex]
new_regexes = [new_regex, new_regex_reverse, transpose(new_regex), list(reversed(transpose(new_regex)))]

total_crosses = 0
for i, line in enumerate(lines[:-2]):
  for regex in new_regexes:
    for m in re.finditer(fr"(?=({regex[0]}))", line):
      if not re.match(regex[1], lines[i+1][m.start():]):
        continue
      if not re.match(regex[2], lines[i+2][m.start():]):
        continue
      total_crosses += 1

print(total, total_crosses)
