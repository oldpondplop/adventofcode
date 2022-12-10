with open('inp.txt', 'r') as f:
    inp = f.read().strip().replace(',', '-').split('\n')

p1 = 0
p2 = 0
for pairs in inp:
    s1, e1, s2, e2 = map(int, pairs.split('-'))
    set1, set2 = map(set, (range(s1, e1 + 1), range(s2, e2 + 1)))
    if set1.issubset(set2) or set2.issubset(set1):
        p1+=1
    if set1 & set2:
        p2+=1

print(p1)
print(p2)
