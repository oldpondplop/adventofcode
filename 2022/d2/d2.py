trans = {'X':'A', 'Y':'B', 'Z':'C'} 
scores = {'A': 1, 'B': 2, 'C': 3}

with open('inp.txt','r') as f:
    inp = f.read().strip()
    for k,v  in trans.items():
        inp = inp.replace(k, v)
    inp = inp.split('\n')

def p1():
    score = 0
    for round in inp:
        p1, p2 = round.split(' ')
        score += scores[p2]
        if p1 == p2:
            score += 3
        elif p1 == 'A': 
            if p2 == 'C': 
                score += 0
            else: 
                score += 6 
        elif p1 == 'B':
            if p2 == 'A':
                score += 0
            else:
                score += 6
        elif p1 == 'C':
            if p2 == 'B':
                score += 0
            else:
                score += 6
    return score

def p2():
    score = 0
    for round in inp:
        p1, p2 = round.split(' ')
        if p1 == p2:
            if p2 == 'A':
                score += 0
                score += scores['C']
            elif p2 == 'B':
                score += 3
                score += scores['B']
            else:
                score += 6
                score += scores['A']
        elif p1 == 'A': 
            if p2 == 'C': 
                score += 6
                score += scores['B']
            else: 
                score += 3
                score += scores['A']
        elif p1 == 'B':
                if p2 == 'A':
                    score += 0
                    score += scores['A']
                else:
                    score += 6
                    score += scores['C']
        elif p1 == 'C':
            if p2 == 'B':
                score += 3
                score += scores['C']
            else:
                score += 0
                score += scores['B']
    return score

print(p1())
print(p2())