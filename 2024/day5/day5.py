import pathlib
from collections import defaultdict
from functools import cmp_to_key
import re

data = pathlib.Path("data.txt").read_text().split("\n\n")
rule_lines = data[0].split("\n")
update_lines = data[1].split("\n")

rules = [[int(i) for i in rule.split("|")] for rule in rule_lines]
updates = [[int(i) for i in update.split(",")] for update in update_lines]
rules_dict = defaultdict(lambda: {"before": [], "after": []})

for before, after in rules:
  rules_dict[before]["after"].append(after)
  rules_dict[after]["before"].append(before)

def comparator(before, after):
  if rules_dict[before]["after"].count(after):
    return -1
  if rules_dict[before]["before"].count(after):
    return 1
    
valid_total = 0
invalid_total = 0
for update in updates:
  update_sorted = list(sorted(update, key=cmp_to_key(comparator)))
  if update == update_sorted: 
    valid_total += update[len(update)//2]
  else:
    invalid_total += update_sorted[len(update_sorted)//2]

print(valid_total, invalid_total)
