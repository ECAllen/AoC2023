import re

class Maps:
    def __init__(self, dst):
        self.dst = dst
        self.maps = []

    def add_map(self, map):
        self.maps.append(map)

    def __repr__(self):
        return f'dst: {self.dst}, maps: {self.maps}'

class Map:
    def __init__(self, src, dst, span):
        self.src = src
        self.dst = dst
        self.span = span
        self.src_start = self.src
        self.src_end= self.src + (self.span - 1)
        self.dst_start = self.dst
        self.dst_end= self.dst + (self.span - 1)

    def inspan(self, n):
        return self.src_start <= n <= self.src_end
   
    def destination(self, n):
        if self.inspan(n):
            return self.dst + (n - self.src_start)    

    def __str__(self):
        return f'src: {self.src}, dst: {self.dst}, span: {self.span}'

    def __repr__(self):
        return f'src: {self.src}, dst: {self.dst}, span: {self.span}'

with open('input.txt', 'r') as f:
    lines = f.readlines()

maps = {}
for line in lines:
    if line.startswith('seeds:'):
        _, seeds = line.split(':')
        seeds = seeds.strip()
        seeds = seeds.split()
        seeds = [int(s) for s in seeds]
        continue

    if 'map:' in line:
        map_pattern = r'(\w+)-to-(\w+) map:'
        src, dst = re.match(map_pattern,line).groups()
        maps[src]=Maps(dst)
    else:
        destination,source,span = line.split() 
        m = Map(int(source), int(destination), int(span))
        maps[src].maps.append(m)
    # print(maps)
locations=[]
for seed in seeds:
    categories = ['seed','soil','fertilizer','water','light','temperature','humidity']
    src = seed
    dest = seed
    for category in categories:
        for m in maps[category].maps:
            if m.inspan(src):
                dest = m.destination(src)
        # print(f"seed: {seed} {category} src: {src} dest: {dest}") 
        src = dest
    locations.append(dest) 
print(min(locations))

# Part 2

import itertools

def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch

lookup = {}
locations=[]
categories = ['seed','soil','fertilizer','water','light','temperature','humidity']
for seed,rng in batched(seeds,2):
    print(f"seed: {seed}, length {rng}")
    for i in range(0,rng):
        sd = seed + i
        src = seed + i
        if lookup.get(src) is not None:
            print(f"hit {i}")
        else:
            for category in categories:
                for m in maps[category].maps:
                    if m.inspan(sd):
                        dest = m.destination(sd)
                        print(f"seed: {seed} src: {src} sd: {sd} i: {i} category: {category} dest: {dest}")
                        sd = dest
                        break
                if category == 'humidity':
                    lookup[i] = sd
            locations.append(lookup[i])
        # break
    # break
    # print(locations)
print(min(locations))

