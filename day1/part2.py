def part2(file):
  curr_freq = 0
  freq_changes = []
  reached_freqs = {0}
    
  with open(file) as f:
    for freq_change in f:
      freq_changes.append(int(freq_change))

  while True:
    for freq in freq_changes:
      curr_freq += freq
      
      if curr_freq in reached_freqs:
        return curr_freq
      
      reached_freqs.add(curr_freq)

if __name__ == '__main__':
  print part2('input.txt')