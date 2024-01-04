from collections import deque

with open('inp.txt','r') as f:
  inp = f.read().strip().split('\n\n')

def p1():
  seeds = list(map(int, inp[0].split(' ', 1)[1].split()))
  mappings = []
  for section in inp[1:]:
    values = [list(map(int, line.split())) for line in section.split('\n')[1:]]
    _map = [(src, src+lenght, dst-src) for dst, src, lenght in values]
    mappings.append(_map)

  location = float('inf')
  for seed in seeds:
    for mapping in mappings:
      for s, e, d in mapping:
        if s <= seed < e:
          seed += d
          break
    location = min(seed, location)
  return location


def p2():
  def _calculate_overlap(seed_interval, mapping_interval):
    """
    seed_interval:    |---------| (s1, e1)
    mapping_interval: |---------| (s2, e2, d)
    
    1. Complete:
      |-----|   (s1, e1)
    |---------| (s2, e2)
    
    2. Inner:
    |---------| (s1, e1)
      |-----|   (s2, e2)
    
    3. Right:
    |-------|   (s1, e1)
      |-------| (s2, e2)
    
    4. Left:
      |------|  (s1, e1)
    |------|    (s2, e2)
    """
    s1, e1 = seed_interval
    s2, e2, d = mapping_interval

    is_left_overlap = (s2 <= s1 < e2)
    is_right_overlap = (s2 < e1 <= e2)
    is_inner_overlap = (s1 < s2 and e1 > e2)

    overlapping, non_overlapping = [], []
    if is_left_overlap and is_right_overlap:  # Complete
      overlapping.append((s1 + d, e1 + d))
    elif is_inner_overlap:  # Inner
      overlapping.append((s2 + d, e2 + d))
      non_overlapping.append((s1, s2))
      non_overlapping.append((e2, e1))
    elif is_right_overlap:  # Right
      overlapping.append((s2 + d, e1 + d))
      non_overlapping.append((s1, s2))
    elif is_left_overlap:  # Left
      overlapping.append((s1 + d, e2 + d))
      non_overlapping.append((e2, e1))
    return overlapping, non_overlapping
  
  seeds = list(map(int, inp[0].split(' ', 1)[1].split()))
  seed_ranges = deque([(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])])
  mappings = []
  for section in inp[1:]:
    values = [list(map(int, line.split())) for line in section.split('\n')[1:]]
    _map = [(src, src+lenght, dst-src) for dst, src, lenght in values]
    mappings.append(_map)
  
  for mapping in mappings:
    new_seed_ranges = deque()
    
    while seed_ranges:
      seed_range = seed_ranges.popleft()
      
      for s, e, d in mapping:
        overlapping, remaining = _calculate_overlap(seed_range, (s, e, d))
        if overlapping: # intersection
          new_seed_ranges.extend(overlapping)
          if remaining: # remaining parts to check against the next mapping
            seed_ranges.extend(remaining)
          break
      else: # no overlapping
        new_seed_ranges.append(seed_range)
        
    seed_ranges = new_seed_ranges
  
  return min(seed_ranges, key=lambda x: x[0])[0]

print(p1())
print(p2())
