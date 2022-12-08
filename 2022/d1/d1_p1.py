with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n\n')

calories = [sum(map(int, g.split('\n'))) for g in inp]

p1 = max(calories)
p2 = sum(sorted(calories)[-3:])
print(p1)
print(p2)