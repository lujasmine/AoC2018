import re

def parse_instructions(file):
  instructions = [[] for _ in range(26)]
  with open(file) as f:
    for instruction in f:
      step  = re.match(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.", instruction)
      first = step.group(1)
      second = step.group(2)

      first_alph_idx = ord(first.lower()) - 97
      second_alph_idx = ord(second.lower()) - 97
      
      if len(instructions[first_alph_idx]) == 0:
        instructions[first_alph_idx].append(-1) 

      instructions[second_alph_idx].append(first_alph_idx)
      if -1 in instructions[second_alph_idx]:
        instructions[second_alph_idx].remove(-1) 

  return instructions

def part1():
  instructions = parse_instructions('input.txt')
  order = []

  while True:
    next_step = ""
    for idx, steps in enumerate(instructions):
      if -1 in steps and steps[1:] == steps[:-1]:
        if idx < next_step:
          next_step = idx
    
    if next_step == "":
      return order

    order.append(next_step)
    instructions[next_step] = []

    for idx, steps in enumerate(instructions):
      if next_step in steps:
        instructions[idx].remove(next_step)
        instructions[idx].insert(0, -1)

def part2(n_steps, n_workers):
  instructions = parse_instructions('input.txt')
  seconds = 0
  worker_timer = [0] * n_workers
  worker_tracker = [None] * n_workers
  n_started = 0

  while True:
    if n_started == n_steps and worker_timer[1:] == worker_timer[:-1]:
      return seconds

    if n_started < len(order):
      for idx, time_left in enumerate(worker_timer):
        for idx2, steps in enumerate(instructions):
          if time_left == 0 and -1 in steps and steps[1:] == steps[:-1]:            
            instructions[idx2] = []
            time = idx2 + 1 + 60
            worker_timer[idx] = time
            worker_tracker[idx] = idx2
            n_started += 1
            break

    for idx, time_left in enumerate(worker_timer):
      if time_left > 0:        
        worker_timer[idx] -= 1
        if worker_timer[idx] == 0: 
          for idx2, steps in enumerate(instructions):
            if worker_tracker[idx] in instructions[idx2]:
              instructions[idx2].remove(worker_tracker[idx])
              instructions[idx2].insert(0, -1)

    seconds += 1
  
if __name__ == '__main__':
  order = part1()
  print(''.join(list(map(lambda step: chr(step + 97).upper(), order))))

  n_workers = 5
  print part2(len(order), n_workers)