def parse_claim_info(file):
  start_points = []
  claim_sizes = []

  with open(file) as f:
    for claim in f:
      claim_id, claim_info = claim.split('@ ')
      start_x, after_start_x = claim_info.split(',')
      start_y, claim_size = after_start_x.split(': ')
      claim_width, claim_height = claim_size.split('x')

      start_points.append((int(start_x), int(start_y)))
      claim_sizes.append((int(claim_width), int(claim_height.strip())))

    return start_points, claim_sizes

def fabric_size(start_points, claim_sizes):
  max_width = 0
  max_height = 0
  
  for (x, y) in start_points:
    for (x_width, y_height) in claim_sizes:
      if x + x_width > max_width:
        max_width = x + x_width
      if y + y_height > max_height:
        max_height = y + y_height

  return max_width, max_height

def process_claims(start_points, claim_sizes, fabric_width, fabric_height):
  fabric_claims = [[0 for x in range(fabric_width)] for y in range(fabric_height)]
  
  for idx, (start_x, start_y) in enumerate(start_points):
    (width, height) = claim_sizes[idx]
    for x in range(width):
      for y in range(height):
        fabric_claims[start_x + x][start_y + y] += 1

  return fabric_claims

def part1(fabric_claims):
  multiple_claims = 0

  for x in range(len(fabric_claims)):
    for y in range (len(fabric_claims[x])):
      if fabric_claims[x][y] > 1:
        multiple_claims += 1

  return multiple_claims

def part2(start_points, claim_sizes, fabric_claims):
  for idx, (start_x, start_y) in enumerate(start_points):
    (width, height) = claim_sizes[idx]

    claim_overlaps = False

    for right in range(width):
      for down in range(height):
        if fabric_claims[start_x + right][start_y + down] > 1:
          claim_overlaps = True

    if not claim_overlaps:
      return idx + 1

if __name__ == '__main__':
  start_points, claim_sizes = parse_claim_info('input.txt')
  fabric_width, fabric_height = fabric_size(start_points, claim_sizes)
  fabric_claims = process_claims(start_points, claim_sizes, fabric_width, fabric_height)

  print part1(fabric_claims)
  print part2(start_points, claim_sizes, fabric_claims)



