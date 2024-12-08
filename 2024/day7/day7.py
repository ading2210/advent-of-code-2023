import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

total_two_ops = 0
total_three_ops = 0

def is_valid(result, equation, base=2):
  for i in range(base ** (len(equation)-1)):
    new_result = equation[0]
    for j in range(1, len(equation)):
      operator = i % base
      i //= base
      if operator == 0:
        new_result += equation[j]
      elif operator == 1:
        new_result *= equation[j]
      else:
        new_result = int(str(new_result) + str(equation[j]))

    if new_result == result:      
      return True
  
  return False

for line in lines:
  result_str, equation_str = line.split(": ")
  result = int(result_str)
  equation = [int(num) for num in equation_str.split()]

  total_two_ops += result * is_valid(result, equation, 2)
  total_three_ops += result * is_valid(result, equation, 3)

print(total_two_ops, total_three_ops)