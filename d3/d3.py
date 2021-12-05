def part1(inp):
    gamma_rate=''
    epsilon_rate=''
    for pos in range(0,12):
        s = ''.join([i[pos] for i in inp])
        most_common = '0' if  s.count('0') > s.count('1') else '1'
        gamma_rate += most_common
        epsilon_rate += '1' if most_common=='0' else '0' 
    return(int(gamma_rate,2) * int(epsilon_rate,2))


def part2(l,pos,arg):
    
    if len(l) == 1:
        return l
    else:
        s = ''.join([i[pos] for i in l])
        most_common = '0' if  s.count('0') > s.count('1') else '1'
        if arg == "most_common":
            filtered = [number for number in l if number[pos]==(most_common)]
        else:
            filtered = [number for number in l if number[pos]!=(most_common)]
        pos+=1
        return part2(filtered,pos,arg)

with open("inp_d3.txt",'r') as f:
    inp = f.read().strip().split("\n")

print(part1(inp))

O2 = part2(inp,0,"most_common")
CO2 = part2(inp,0,"least_common")

print(int(*CO2,2) * int(*O2,2))
