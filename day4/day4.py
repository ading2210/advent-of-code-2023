import re
import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

def get_matches(line):
  line = line.replace(":", "|")
  _, winning_str, nums_str = line.split("|")
  
  winning_nums = [int(s) for s in winning_str.split()]
  card_nums = [int(s) for s in nums_str.split()]
  common_nums = list(set(winning_nums).intersection(card_nums))

  return len(common_nums)

def part1():
  total = 0
  for line in lines:
    matches = get_matches(line)
    if matches > 0:
      total += 2 ** (matches - 1)

  print(total)

def part2():
  all_cards = []
  for line in lines:
    all_cards.append([1, line])
  
  for i, line in enumerate(lines):
    copies, card = all_cards[i]
    matches = get_matches(line)

    for j in range(i+1, i+1+matches):
      if j >= len(lines): continue
      all_cards[j][0] += copies
  
  total = 0
  for copies, card in all_cards:
    total += copies
  
  print(total)

part2()