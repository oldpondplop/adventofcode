def part1(inp):
    depth=0
    horizontal=0
    for i in inp:
        val = int(i[-1])
        if i.__contains__('forward'):
            horizontal+=val
        elif i.__contains__('up'):
            depth-=val
        else: depth+=val
    print(depth*horizontal)

def part2(inp):
    aim=0
    depth=0
    horizontal=0
    for i in inp:
        val = int(i[-1])
        if i.__contains__('forward'):
            horizontal+=val
            depth+=(aim*val)
        elif i.__contains__('up'):
            aim-=val
        else: aim+=val
    print(depth*horizontal)

with open("inp_d2.txt",'r') as f:
    inp = f.read().strip().split("\n")

part1(inp)
part2(inp)
