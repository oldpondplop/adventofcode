from pathlib import Path
from collections import defaultdict
from itertools import groupby

with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n')

p = Path('/')
d = defaultdict(int)
for k, g in groupby(inp, lambda x: x.startswith("$ cd")):    
    g = list(g)
    if k:
        for i in g:
            p = p / i.split()[-1]
    else:
        d[p.resolve()] = sum(int(i.split()[0]) for i in g if i[0].isdigit())

for p in d.keys():
    if p.parent != p:
        # print(f'{p.parent} {d[p.parent]} {p} {d[p]}')
        d[p.parent] += d[p]

p1 = sum(v for v in d.values() if v <= 100000)

print(p1)