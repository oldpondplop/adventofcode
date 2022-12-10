with open('inp.txt','r') as f:
    inp = f.read().strip()

def solution(marker):
    for i in range(1, len(inp) - marker):
        e = i + marker
        if len(set(inp[i:e])) == marker:
            return e

p1 = solution(4)
p2 = solution(14)

print(p1)
print(p2)