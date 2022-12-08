def analysis(patterns):
    d = {}

    unique = {
        2 : 1,
        3 : 7,
        4 : 4,
        7 : 8
    }

    for p,l in patterns:
        if l in unique:
            k = unique[l]
            d[k] = p

    for p,l in patterns:
        if p in d.values():
            continue

        if l == 6: #[0,6,9]
            if len(d[1] & p) == 1:
                d[6] = p
            elif len(d[4] & p) == 4:
                d[9] = p
            else: 
                d[0] = p

        elif l == 5: #[2,3,5]
            if len(d[1] & p) == 2:
                d[3] = p
            elif len(d[4] & p) == 3:
                d[5] = p
            else: 
                d[2] = p
    return d

with open('inp_d8.txt','r') as f:
    inp = f.read().strip().split('\n')

total, count = 0, 0
for line in inp:
    patterns, digits = map(str.split, line.split(' | '))
    patterns = tuple(map(lambda x: (frozenset(x), len(x)), patterns))
    digits = tuple(map(frozenset, digits))

    d_vk= {v: k for k, v in analysis(patterns).items()}

    value, i = 0, 1000
    for digit in digits: 
        total += d_vk[digit] * i
        i //= 10
    
    total += value
    count += sum(len(word) in (2, 3, 4, 7) for word in digits)

print("Part 1:", count)
print("Part 2:", total)