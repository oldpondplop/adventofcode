from collections import deque
from collections import defaultdict


with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n')

d = defaultdict(int)
stack = []
for e in inp:
    if e.startswith('$ cd') and '..' not in e:
            cwd = e.split()[-1]
            p = stack.pop() if stack else ()
            pwd = (*p, cwd) 
            stack.append(pwd)
    elif '..' in e:
        stack = [stack.pop()[:-1]]
    elif e[0].isdigit():
        dir_total = int(e.split()[0])
        d[pwd] += dir_total
        for i in range(1, len(pwd)):
            d[pwd[:-i]] += dir_total

p1 = sum(v for v in d.values() if v <= 100000)

size = 30000000 - (70000000 - d[('/',)])
p2 = [i for i in sorted(d.values()) if i >= size][0]

print(p1)
print(p2)