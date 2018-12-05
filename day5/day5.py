from string import ascii_lowercase

def read_input(file):
  with open(file) as f:
    return f.readline().strip()

def part1(polymer):
  before_next_reaction = polymer
  after_reaction = ""

  while after_reaction != before_next_reaction:
    after_reaction = before_next_reaction

    for char in after_reaction:
      after_reaction = after_reaction.replace(char.lower() + char.upper(), '') \
        .replace(char.upper() + char.lower(), '')
      before_next_reaction = after_reaction

  return len(after_reaction)

def part2(polymer):
  shortest_polymer = len(polymer)

  for polymer_type in ascii_lowercase:
    removed_polymer_type = polymer.replace(polymer_type, '').replace(polymer_type.upper(), '')
    after_reaction_length = part1(removed_polymer_type)

    if after_reaction_length < shortest_polymer:
      shortest_polymer = after_reaction_length

  return shortest_polymer


if __name__ == '__main__':
  polymer = read_input('input.txt')
  print part1(polymer)
  print part2(polymer)


