from pathlib import Path
from collections import defaultdict
wd = Path(__file__).parent

with open(wd / 'inp.txt','r') as f:
  inp = f.read().strip().split('\n\n')

def p1():
  seeds = list(map(int, inp[0].split(' ', 1)[1].split()))
  mappings = []
  for section in inp[1:]:
    values = [list(map(int, line.split())) for line in section.split('\n')[1:]]
    _map = [(src, src+lenght, dst-src) for dst, src, lenght in values]
    mappings.append(_map)

  location = float('inf')
  for seed in seeds:
    for maps in mappings:
      for s, e, d in maps:
        if s <= seed < e:
          seed += d
          break
  
    if seed < location:
      location = seed
  
  return location

# print(p1())


"""
seed-to-soil map: source-destination
50 98 2 -> dest, source, lenght (source 98: dest 50) [50, 51] -> [98, 99] (seed 98-> soil 50) | list(range(dest, dest+lenght)
52 50 48 -> dest, source, lenght (source 50: dest 52) [50, 51 ... 96, 97] -> [52, 53 ..., 98, 99] (seed 53->soil 55)
"""

inp = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().split('\n\n')


seeds = list(map(int, inp[0].split(' ', 1)[1].split()))
seeds = list(zip(seeds[::2], seeds[1::2]))
print(seeds)
mappings = []
for section in inp[1:]:
  values = [list(map(int, line.split())) for line in section.split('\n')[1:]]
  _map = [(src, src+lenght, dst-src) for dst, src, lenght in values]
  mappings.append(_map)


seed_mapping = defaultdict(lambda: defaultdict(lambda: None))
section_mapping = {
  0: 'soil',
  1: 'fertilizer',
  2: 'water',
  3: 'light',
  4: 'temperature',
  5: 'humidity',
  6: 'location'
}

location = float('inf')
for ss, l in seeds:
  for seed in range(ss, ss+l):
    k = seed
    for i, maps in enumerate(mappings):
      for s, e, d in maps:
        if s <= seed < e:
          seed += d
          seed_mapping[k][section_mapping[i]] = seed
          seed_mapping[k][7] = range(s, s + e), maps
          break
      else:
        seed_mapping[k][section_mapping[i]] = seed
        seed_mapping[k][7] = maps
    
    if seed < location:
      location = seed

for seed, values in seed_mapping.items():
  print(f"Seed {seed}, soil {values['soil']}, fertilizer {values['fertilizer']}, water {values['water']}, light {values['light']}, temperature {values['temperature']}, humidity {values['humidity']}, location {values['location']} {values[7]}")

print(location)


