def part2(file):
  box_ids = []
  with open(file) as f:
    for box_id in f:
      box_ids.append(box_id.strip())

  for box_id in box_ids:
    for box_id_2 in box_ids:
      common_letters = []

      for idx, char in enumerate(box_id):
        if char == box_id_2[idx]:
          common_letters.append(char)

      if len(common_letters) == len(box_id) - 1:
        return ''.join(common_letters)

if __name__ == '__main__':
  print part2('input.txt')
