with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n')

w2i = {
  'one'  : 1,
  'two'  : 2,
  'three': 3,
  'four' : 4,
  'five' : 5,
  'six'  : 6,
  'seven': 7,
  'eight': 8,
  'nine' : 9,
}

def p1():
  total = 0
  for line in inp:
    for c in line:
      if c.isdigit():
        total += int(c) * 10
        break
    for c in line[::-1]:
      if c.isdigit():
        total += int(c)
        break 
  return total

def p2():
  def _get_digit(s: str):
    c = s[-1]
    if c.isdigit():
      return int(c)
    for d in w2i:
      if s.endswith(d):
        return w2i[d]
    
  total = 0
  for line in inp:
    for i in range(1, len(line) + 1):
      d1 = _get_digit(line[:i])
      if d1:
        total += d1 * 10
        break

    for i in range(len(line), 0, -1):
      d2 = _get_digit(line[:i])
      if d2:
        total += d2
        break
  return total

print(p1())
print(p2())