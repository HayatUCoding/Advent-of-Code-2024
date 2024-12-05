file = open("day4/input.txt", "r")



def part_one():
  character_list = []
  XMAS_found = 0

  for line in file:
    character_list.append(line)
  character_list_length = len(character_list) - 1
  line_list_length = len(character_list[0]) - 1

  def check_N(index_list, index_char, XMAS_found):
    if index_list - 3 >= 0:
      if character_list[index_list-1][index_char] == "M":
        if character_list[index_list-2][index_char] == "A":
          if character_list[index_list-3][index_char] == "S":
            XMAS_found += 1
    return XMAS_found

  def check_E(index_list, index_char, XMAS_found):
    if line_list_length >= index_char + 3:
      if character_list[index_list][index_char+1] == "M":
        if character_list[index_list][index_char+2] == "A":
          if character_list[index_list][index_char+3] == "S":
            XMAS_found += 1
    return XMAS_found

  def check_S(index_list, index_char, XMAS_found):
    if character_list_length >= index_list + 3:
      if character_list[index_list+1][index_char] == "M":
        if character_list[index_list+2][index_char] == "A":
          if character_list[index_list+3][index_char] == "S":
            XMAS_found += 1
    return XMAS_found

  def check_W(index_list, index_char, XMAS_found):
    if index_char - 3 >= 0:
      if character_list[index_list][index_char-1] == "M":
        if character_list[index_list][index_char-2] == "A":
          if character_list[index_list][index_char-3] == "S":
            XMAS_found += 1
    return XMAS_found

  def check_NE(index_list, index_char, XMAS_found):
    if index_list - 3 >= 0:
      if line_list_length >= index_char + 3:
        if character_list[index_list-1][index_char+1] == "M":
          if character_list[index_list-2][index_char+2] == "A":
            if character_list[index_list-3][index_char+3] == "S":
              XMAS_found += 1
    return XMAS_found

  def check_SE(index_list, index_char, XMAS_found):
    if character_list_length >= index_list + 3:
      if line_list_length >= index_char + 3:
        if character_list[index_list+1][index_char+1] == "M":
          if character_list[index_list+2][index_char+2] == "A":
            if character_list[index_list+3][index_char+3] == "S":
              XMAS_found += 1
    return XMAS_found

  def check_SW(index_list, index_char, XMAS_found):
    if character_list_length >= index_list + 3:
      if index_char - 3 >= 0:
        if character_list[index_list+1][index_char-1] == "M":
          if character_list[index_list+2][index_char-2] == "A":
            if character_list[index_list+3][index_char-3] == "S":
              XMAS_found += 1
    return XMAS_found

  def check_NW(index_list, index_char, XMAS_found):
    if index_list - 3 >= 0:
      if index_char - 3 >= 0:
        if character_list[index_list-1][index_char-1] == "M":
          if character_list[index_list-2][index_char-2] == "A":
            if character_list[index_list-3][index_char-3] == "S":
              XMAS_found += 1
    return XMAS_found



  for index_list, item in enumerate(character_list):
    for index_char, char in enumerate(item):
      if char == "X":
        XMAS_found = check_N(index_list, index_char, XMAS_found)
        XMAS_found = check_E(index_list, index_char, XMAS_found)
        XMAS_found = check_S(index_list, index_char, XMAS_found)
        XMAS_found = check_W(index_list, index_char, XMAS_found)
        XMAS_found = check_NE(index_list, index_char, XMAS_found)
        XMAS_found = check_SE(index_list, index_char, XMAS_found)
        XMAS_found = check_SW(index_list, index_char, XMAS_found)
        XMAS_found = check_NW(index_list, index_char, XMAS_found)

  return XMAS_found


def part_two():
  character_list = []
  XMAS_found = 0

  for line in file:
    character_list.append(line)
  character_list_length = len(character_list) - 1
  line_list_length = len(character_list[0]) - 1

  def check_NE(index_list, index_char, XMAS_found):
    if index_list - 2 >= 0:
      if line_list_length >= index_char + 2:
        if character_list[index_list-1][index_char+1] == "A":
          if character_list[index_list-2][index_char+2] == "S":
            if character_list[index_list-2][index_char] == "M":
              if character_list[index_list][index_char+2] == "S":
                XMAS_found += 1
    return XMAS_found

  def check_SE(index_list, index_char, XMAS_found):
    if character_list_length >= index_list + 2:
      if line_list_length >= index_char + 2:
        if character_list[index_list+1][index_char+1] == "A":
          if character_list[index_list+2][index_char+2] == "S":
            if character_list[index_list][index_char+2] == "M":
              if character_list[index_list+2][index_char] == "S":
                XMAS_found += 1
    return XMAS_found

  def check_SW(index_list, index_char, XMAS_found):
    if character_list_length >= index_list + 2:
      if index_char - 2 >= 0:
        if character_list[index_list+1][index_char-1] == "A":
          if character_list[index_list+2][index_char-2] == "S":
            if character_list[index_list+2][index_char] == "M":
              if character_list[index_list][index_char-2] == "S":
                XMAS_found += 1
    return XMAS_found

  def check_NW(index_list, index_char, XMAS_found):
    if index_list - 2 >= 0:
      if index_char - 2 >= 0:
        if character_list[index_list-1][index_char-1] == "A":
          if character_list[index_list-2][index_char-2] == "S":
            if character_list[index_list][index_char-2] == "M":
              if character_list[index_list-2][index_char] == "S":
                XMAS_found += 1
    return XMAS_found



  for index_list, item in enumerate(character_list):
    for index_char, char in enumerate(item):
      if char == "M":
        XMAS_found = check_NE(index_list, index_char, XMAS_found)
        XMAS_found = check_SE(index_list, index_char, XMAS_found)
        XMAS_found = check_SW(index_list, index_char, XMAS_found)
        XMAS_found = check_NW(index_list, index_char, XMAS_found)
  

  return XMAS_found

print(part_two())