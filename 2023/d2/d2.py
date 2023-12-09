with open('inp.txt','r') as f:
  inp = f.read().strip().split('\n')

def p1():
  total = 0
  for line in inp:
    id, game = line.split(': ')
    id = int(id.split()[-1])
    sets = game.split("; ")
    possible = True
    for s in sets:
      for n, color in map(str.split, s.split(', ')):
        n = int(n)
        if (n > 14 and color == 'blue') or (n > 13 and color == 'green') or (n > 12 and color == 'red'):
          possible = False
    if possible:
      total += id
  return total

def p2():
  total = 0
  for line in inp:
    id, game = line.split(': ')
    id = int(id.split()[-1])
    sets = game.split("; ")
    r, b, g = 0, 0, 0
    for s in sets:
      for n, color in map(str.split, s.split(', ')):
        n = int(n)
        if color == 'blue':
          b = max(b, n)
        if color == 'green':
          g = max(g, n)
        if color == 'red':
          r = max(r, n)
    total += r * g * b
  return total

print(p1())
print(p2())