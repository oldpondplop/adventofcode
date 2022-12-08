with open("inp_d1.txt") as f:
    inp = [int(i) for i in f.read().strip().split('\n')]

#fuglede
print(sum(i1<i2 for i1,i2 in zip(inp,inp[1:])))
print(sum(i1<i2 for i1,i2 in zip(inp,inp[3:])))
