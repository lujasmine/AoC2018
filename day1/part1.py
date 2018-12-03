def part1(file):
  curr_freq = 0
  with open(file) as f:
      for freq_change in f:
        curr_freq += int(freq_change)
  return curr_freq

if __name__ == '__main__':
  print part1('input.txt')