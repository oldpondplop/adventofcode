from collections import deque

with open('inp_d6.txt','r') as f:
    cnt = deque(map(f.read().count, "012345678"))

for d in range(1,257):

    cnt.rotate(-1)
    cnt[6] += cnt[8]

    if d == 80 or d == 256:
        print(sum(cnt))