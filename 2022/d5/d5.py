with open('inp.txt','r') as f:
    inp = f.read().split('\n\n')

grid, instr = [i.split('\n') for i in inp]
cols = list(zip(*grid))
stacks = [''.join(cols[n]).lstrip()[:-1] for n in range(len(cols)) if n % 4 == 1]

def p1():
    for i in instr:
        if i:
            q, _from, to = [int(i) for i in i.split()[1::2]]
            _from -= 1
            to -= 1
            crates = stacks[_from][:q][::-1]
            stacks[_from] = stacks[_from][q:]
            stacks[to] = crates + stacks[to]

    return ''.join(*zip(*stacks))

def p2():
    for i in instr:
        if i:
            q, _from, to = [int(i) for i in i.split()[1::2]]
            _from -= 1
            to -= 1
            crates = stacks[_from][:q]
            stacks[_from] = stacks[_from][q:]
            stacks[to] = crates + stacks[to]

    return ''.join(*zip(*stacks))

print(p1())
print(p2())