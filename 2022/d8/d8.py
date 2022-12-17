def dist(l):
    d = 0
    for tree in l:
        if ego > tree: 
            d += 1
        elif ego >= tree: 
            d += 1
            return d
    return d

with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n')
    inp = [list(map(int, list(l))) for l in inp]

size = len(inp)
m, n = size - 1, size - 1
visible = m * 2 + n * 2
scenic_score = 0

for i in range(1, m):
    for j in range(1, n):
        ego = inp[i][j]
        lr, rr = inp[i][:j], inp[i][j+1:]
        bc =  [inp[c+1][j] for c in range(i, n)]
        tc = [inp[c][j] for c in range(0, i)] 
        
        if (ego > max(lr) or ego > max(rr) or ego > max(bc) or ego > max(tc)):
            
            visible += 1
            
            ego_score = dist(lr[::-1]) * dist(rr) * dist(bc) * dist(tc[::-1])
            
            if ego_score > scenic_score:
                scenic_score = ego_score
p1 = visible
p2 = scenic_score

print(p1)
print(p2)