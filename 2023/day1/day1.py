import re
import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def part1():
  total = 0
  for line in lines:
    digits = [int(char) for char in line if char.isdigit()]
    total += 10 * digits[0]
    total += digits[-1]
  
  print(total)

def part2():
  total = 0
  for line in lines:
    digit_regex = r'(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))'
    matches = re.findall(digit_regex, line)

    digit_a = matches[0]
    digit_b = matches[-1]

    if digit_a.isdigit():
      line_result = 10 * int(digit_a)
    else:
      line_result = 10 * (digit_words.index(digit_a) + 1)
    
    if digit_b.isdigit():
      line_result += int(digit_b)
    else:
      line_result += digit_words.index(digit_b) + 1
    
    total += line_result

  print(total)
  
part2()