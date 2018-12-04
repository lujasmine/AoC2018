import re

def sort_entries_from_file(file):
  entries = set()

  with open(file) as f:
    for entry in f:
      entries.add(entry.strip())

  return sorted(entries)

""" Generates a guard sleep schedule

A dictionary is used to store this information, with structure:
- Key: guard id
- Value: array of length 60, with the number in each index determining 
  how many times on that minute the guard is asleep
"""
def get_guard_sleep_schedule(entries):
  guard_sleep_schedule = {}
  guard_id = -1
  falls_asleep_minute = -1
  wakes_up_minute = -1

  for entry in entries:
    new_guard = re.match(r"\[.*\] Guard #(\d*) begins shift", entry)
    if new_guard:
      guard_id = new_guard.group(1)

      if guard_id not in guard_sleep_schedule:
        guard_sleep_schedule[guard_id] = [0] * 60

    falls_asleep = re.match(r"\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\] falls asleep", entry)
    if falls_asleep:
      falls_asleep_minute = int(falls_asleep.group(1))

    wakes_up = re.match(r"\[\d\d\d\d-\d\d-\d\d \d\d:(\d\d)\] wakes up", entry)
    if wakes_up:
      wakes_up_minute = int(wakes_up.group(1))
      for minute in range(falls_asleep_minute, wakes_up_minute):
        guard_sleep_schedule[guard_id][minute] += 1
  
  return guard_sleep_schedule

def get_most_asleep_guard(guard_sleep_schedule):
  most_asleep_guard = -1
  most_asleep_minutes = 0
  
  for guard_id, sleep_array in guard_sleep_schedule.iteritems():
    if sum(sleep_array) > most_asleep_minutes:
      most_asleep_minutes = sum(sleep_array)
      most_asleep_guard = guard_id

  return most_asleep_guard

def index_of_max_in_array(array):
  return array.index(max(array))
      
def part1(guard_sleep_schedule):
  sleepiest_guard = get_most_asleep_guard(guard_sleep_schedule)
  most_asleep_minute = index_of_max_in_array(guard_sleep_schedule[sleepiest_guard])
  
  return int(sleepiest_guard) * most_asleep_minute

def part2(guard_sleep_schedule):
  most_spent_asleep_minute = -1
  guard = -1
  max_num_days_asleep_for_minute = 0

  for guard_id, sleep_array in guard_sleep_schedule.iteritems():
    most_asleep_minute = index_of_max_in_array(sleep_array)
    num_days_asleep_on_minute = sleep_array[most_asleep_minute]
    
    if num_days_asleep_on_minute > max_num_days_asleep_for_minute:
      max_num_days_asleep_for_minute = num_days_asleep_on_minute
      guard = guard_id
      most_spent_asleep_minute = most_asleep_minute

  return int(guard) * most_spent_asleep_minute

if __name__ == '__main__':
  sorted_entries = sort_entries_from_file('input.txt')
  guard_sleep_schedule =  get_guard_sleep_schedule(sorted_entries)

  print part1(guard_sleep_schedule)
  print part2(guard_sleep_schedule)