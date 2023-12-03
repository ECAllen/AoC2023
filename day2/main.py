import re
# First problem
# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes 
# 13 green cubes 
# 14 blue cubes 
# What is the sum of the IDs of those games?


with open('input.txt') as f:
    data = f.read().splitlines()

total = 0
for line in data:
    game, plays = line.split(':')

    red_re = re.compile(r'(\d+) red')
    blue_re = re.compile(r'(\d+) blue')
    green_re= re.compile(r'(\d+) green')

    reds = [int(r) for r in red_re.findall(plays)]
    blues = [int(r) for r in blue_re.findall(plays)]
    greens = [int(r) for r in green_re.findall(plays)]

    # print(plays)
    # print(reds, blues, greens)

    if True in [r > 12 for r in reds]:
        continue 
    if True in [g > 13 for g in greens]:
        continue 
    if True in [b > 14 for b in blues]:
        continue 

    game_re = re.compile(r'Game (\d+)')
    game_num = int(game_re.findall(game)[0])
    
    total += game_num

print(total)

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of 
# the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these 
# five powers produces the sum 2286.

# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

total = 0
for line in data:
    game, plays = line.split(':')

    red_re = re.compile(r'(\d+) red')
    blue_re = re.compile(r'(\d+) blue')
    green_re= re.compile(r'(\d+) green')

    reds = max([int(r) for r in red_re.findall(plays)])
    blues = max([int(r) for r in blue_re.findall(plays)])
    greens = max([int(r) for r in green_re.findall(plays)])

    total += reds*blues*greens

print(total)








