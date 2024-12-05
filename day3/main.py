import re


file = open("day3/input.txt", "r")
instructions = file.read()


def part_one():
  x = re.findall("mul\(\d+,\d+\)", instructions)

  total = 0
  for item in x:
    y = re.findall("\d+", item)
    total  += int(y[0]) * int(y[1])

  return total


def part_two():
  x = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", instructions)
  delete = False
  cleaned_list = []
  total = 0

  for i, item in enumerate(x):
    if item == "don't()":
      delete = True
    if item == "do()":
      delete = False
      x[i] = "mul(1,0)"
    if delete == False:
      cleaned_list.append(x[i])
    print(cleaned_list)

  for item in cleaned_list:
    y = re.findall("\d+", item)
    total  += int(y[0]) * int(y[1])

  return total


print(part_two())