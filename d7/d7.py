def part1(p,l):
    return sum(abs(i-p) for i in l)

def part2(p,l):
    return int(sum(abs(i-p)*(abs(i-p)+1)/2 for i in l))

def result(fun):
    lowest = float('inf')
    for p in range(min(ns), max(ns)): 
        fuel = fun(p,ns)
        if fuel < lowest: 
            lowest = fuel
    return lowest

with open('inp_d7.txt','r') as f:
    ns = list(map(int, f.read().strip().split(',')))


print('Part 1:',result(part1))
print('Part 2:',result(part2))