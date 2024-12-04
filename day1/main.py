file = open("day1/input.txt", "r")
list_1 = []
list_2 = []
list_final = []

for line in file:
  split_line = line.split()
  list_1.append(int(split_line[0]))
  list_2.append(int(split_line[1]))



def part_one():
  list_1.sort()
  list_2.sort()

  i = 0
  for number in list_1:
    difference = number - list_2[i]
    if difference < 0:
      difference *= -1
    list_final.append(difference)
    i += 1

  return sum(list_final)


def part_two():
  similarity_score = 0

  for number in list_1:
    number_counted = list_2.count(number)
    similarity_score += number_counted * number

  return similarity_score

print(part_two())