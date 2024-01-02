with open('inp.txt','r') as f:
  inp = f.read().strip().split('\n')

def p1():
  total = 0
  for card in inp:
    _, numbers = card.split(': ')
    win_numbers, my_numbers = [set(map(int, x.split())) for x in numbers.split(" | ")]
    matches = len(win_numbers & my_numbers)
    total += 2 ** (matches - 1) if matches else 0
  return total

def p2():
  d = {k: 1 for k in range(len(inp))}
  for i, card in enumerate(inp):
    _, numbers = card.split(': ')
    win_numbers, my_numbers = [set(map(int, x.split())) for x in numbers.split(" | ")]
    copies = len(win_numbers & my_numbers)
    for j in range(i, i + copies):
      d[j + 1] += d[i]

  total = sum(d.values())
  return total

print(p1())
print(p2())