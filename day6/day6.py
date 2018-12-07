def parse_coords(file):
  coords = []
  with open(file) as f:
    for coord in f:
      x, y = coord.split(',')
      coords.append((int(x), int(y)))

  return coords

def calc_grid_size(coords):
  max_width = 0
  max_height = 0

  for (x, y) in coords:
    if x + 1 > max_width:
      max_width = x + 1
    if y + 1 > max_height:
      max_height = y + 1

  return max_width, max_height

def calc_manhattan_dist(point1, point2):
  return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def grid_with_distances(coords):
  width, height = calc_grid_size(coords)

  # init grid with tuple representing coordinate index with min manhattan distance (coord, min_dist)
  grid = [[(-1, width + height) for x in range(width + 1)] for y in range(height + 1)]

  for x in range(width):
    for y in range(height):
      for idx, coord in enumerate(coords):
        curr_min_dist = grid[y][x][1]
        manhattan_dist = calc_manhattan_dist(coord, (x, y))

        if manhattan_dist < curr_min_dist:
          grid[y][x] = (idx, manhattan_dist)
        elif manhattan_dist == curr_min_dist:
          grid[y][x] = (-1, manhattan_dist)

  return grid

def is_edge(coord, grid):
  return coord[0] == len(grid[0]) - 1 and coord[1] == len(grid) - 1 or coord[0] == 0 or coord[1] == 0

def part1(coords):
  grid = grid_with_distances(coords)
  areas = [0] * len(coords)

  for x in range(len(grid[0])):
    for y in range(len(grid)):
      
      closest_coord = grid[y][x][0]
      if is_edge((x, y), grid):
        areas[closest_coord] = -1
      
      if areas[closest_coord] != -1:
        areas[closest_coord] += 1

  return max(areas)

def part2(coords):
  width, height = calc_grid_size(coords)
  region_size = 0

  for x in range(width):
    for y in range(height):
      sum_distance = 0
      for coord in coords:
        sum_distance += calc_manhattan_dist(coord, (x, y))
      
      if sum_distance < 10000:
        region_size += 1

  return region_size

if __name__ == '__main__':
  coords = parse_coords('input.txt')
  print part1(coords)
  print part2(coords)