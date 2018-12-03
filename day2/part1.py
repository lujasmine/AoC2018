def part1(file):
  twice = 0
  thrice = 0

  with open('input.txt') as f:
    for box_id in f:
      occured_chars = set()

      twice_occured = False
      thrice_occured = False

      for char in box_id:
        if char not in occured_chars:
          occured_chars.add(char)
          count = box_id.count(char)

          if count == 2 and not twice_occured:
            twice_occured = True
            twice += 1
          elif count == 3 and not thrice_occured:
            thrice +=1
            thrice_occured = True

        count = 0
        
  return twice * thrice

if __name__ == '__main__':
  print part1('input.txt')
      