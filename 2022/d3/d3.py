from itertools import islice

with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n')

def p1():
    psum = 0
    for i in inp:
        n = len(i) // 2
        s1, s2 = i[:n], i[:n]
        common = list(set(s1) & set(s2))[0]
        priority = (ord(common) - 38, ord(common) - 96)[common.islower()]
        psum += priority
    return psum

def p2():
    psum = 0
    sets = map(set, inp)
    for _ in range(len(inp) // 3):
        common = list(set.intersection(*islice(sets, 3)))[0]
        priority = (ord(common) - 38, ord(common) - 96)[common.islower()]
        psum += priority
    return psum
    
print(p1(), p2())