file = open("day2/input.txt", "r")

def level_check(split_line):
  safety_check = True
  number_previous = ""
  ascending_check = False

  for number in split_line:
    number = int(number)
    if number_previous == "":
       number_previous = number
       if number - int(split_line[1]) < 0:
         ascending_check = True
       continue
     
    number_difference = number_previous - number
    number_previous = number
    if ascending_check == True:
      if number_difference <= -4 or number_difference >= 0:
        safety_check = False
    else:
      if number_difference >= 4 or number_difference <= 0:
        safety_check = False
  
  return safety_check


def part_one():
  safe_count = 0

  for line in file:
    split_line = line.split()
    safety_check = level_check(split_line)


    if safety_check == True:
      safe_count += 1
  
  return safe_count


def part_two():
  safe_count = 0

  for line in file:
    pd_split_line = []
    split_line = line.split()
    safety_check = level_check(split_line)

    if safety_check != True:
      for i in range(len(split_line)):
        temp_destruct_split_line = list(split_line)
        temp_destruct_split_line.pop(i)
        pd_split_line.append(temp_destruct_split_line)

      for i in range(len(pd_split_line)):
        safety_check = level_check(pd_split_line[i])
        if safety_check == True:
          break

    if safety_check == True:
      safe_count += 1


  return safe_count

print("safe count:",part_two())
