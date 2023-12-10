from collections import defaultdict

with open('inp.txt','r') as f:
  inp = f.read().strip().split('\n')


def p1():
  def _is_part_num(x: int, y: int, e: int, w: int, h: int):
    not_symbols = '.0123456789'
    s = (x - 1) if x >= 1 else 0
    e = (e + 1) if e < w - 1  else w
    for i in range(s, e):
      if inp[y][i] not in not_symbols: # curr
        return True
      if y > 0 and inp[y - 1][i] not in not_symbols: # up
        return True
      if y < h - 1 and  inp[y + 1][i] not in not_symbols: # down
        return True
    return False
    
  def _get_number(row: str, x: int, w: int):
    i = x + 1
    while i < w and row[i].isdigit():
      i += 1 
    return int(row[x: i]), i - 1

  w, h = len(inp[0]), len(inp) 
  total = 0
  for y, row in enumerate(inp):
    x = 0
    while x < w:      
      if row[x].isdigit():
        num, end = _get_number(row, x, w)
        if _is_part_num(x, y, end + 1, w, h):
          total += num
        x = end
      x += 1
  return total

def p2():
  def _is_part_num(x: int, y: int, e: int, w: int, h: int):
    not_symbols = '.0123456789'
    s = (x - 1) if x >= 1 else 0
    e = (e + 1) if e < w - 1  else w
    gears = []
    is_part_num = False 
    for i in range(s, e):
      if inp[y][i] not in not_symbols: # curr
        if inp[y][i] == '*':
          gears.append((y, i))
          is_part_num = True
      if y > 0 and inp[y - 1][i] not in not_symbols: # up
        if inp[y - 1][i] == '*':
          gears.append((y - 1, i))
          is_part_num = True
      if y < h - 1 and  inp[y + 1][i] not in not_symbols: # down
        if inp[y + 1][i] == '*':
          gears.append((y + 1, i))
          is_part_num = True
    return is_part_num, gears
    
  def _get_number(row: str, x: int, w: int):
    i = x + 1
    while i < w and row[i].isdigit():
      i += 1 
    return int(row[x: i]), i - 1

  gears = defaultdict(list)
  w, h = len(inp[0]), len(inp) 
  total = 0
  for y, row in enumerate(inp):
    x = 0
    while x < w:      
      if row[x].isdigit():
        num, end = _get_number(row, x, w)
        is_part_num, gears_coords = _is_part_num(x, y, end + 1, w, h)
        if is_part_num:
          for gc in gears_coords:
            gears[gc].append(num)
        x = end
      x += 1
  for part_nums in gears.values():
    if len(part_nums) == 2:
      total += part_nums[0] * part_nums[1]  
  return total


print(p1())
print(p2())