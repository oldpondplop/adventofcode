def part1(inp):
    increased = 0
    for i in range(0, len(inp) - 1):
        if inp[i] < inp[i + 1]:
            increased += 1
    print(increased)


def part2(inp):
    increased = 0
    prev = 0
    for i in range(0, len(inp) - 2):
        three = sum(inp[i : i + 3])
        if prev < three and prev != 0:
            increased += 1
        prev = three
    print(increased)


with open("inp_d1.txt", "r") as f:
    inp = f.read().strip().split("\n")

inp = [int(i) for i in inp]

part1(inp)
part2(inp)
