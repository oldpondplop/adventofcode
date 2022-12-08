from collections import defaultdict
from itertools import repeat,starmap,chain

def rng(a, b):
    if a > b:
        yield from range(a, b - 1, -1)
    else: 
        yield from range(a, b + 1)

def part1(x1, y1, x2, y2):
    if x1 == x2:
        yield from zip(rng(y1, y2), repeat(x1))

    elif y1 == y2:
        yield from zip(repeat(y1), rng(x1, x2))

def part2(x1, y1, x2, y2):
    if x1 != x2 and y1 != y2:
        yield from zip(rng(y1, y2), rng(x1, x2))


with open('inp_d5.txt','r') as f:
    ns = [[int(i) for i in l.split(',')] for l in f.read().strip().replace('->',',').split('\n')]

d = defaultdict(int)

for y,x in chain(*starmap(part1, ns)):
   d[y,x] += 1

print('part1:', sum(v > 1 for v in d.values()))

for y,x in chain(*starmap(part2, ns)):
   d[y,x] += 1
   
print('part2:', sum(v > 1 for v in d.values()))