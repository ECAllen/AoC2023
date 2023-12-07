
races = [(45,305), (97,1062), (72,1110), (95,1695)]

total = 1
for race in races:
    time, race_distance = race
    print(f"time: {time}, distance: {race_distance}")

    winning_distances = []
    for hold in range(0,time+1):
        distance =(time-hold)*hold
        if distance > race_distance:
            winning_distances.append(distance)
        # print(f"time: {time} race distance: {race_distance} hold: {hold} distance: {distance}")
    total *= len(winning_distances)
print(total)

# Part 2

total = 1
time = 45977295
race_distance = 305106211101695
print(f"time: {time}, distance: {race_distance}")

winning_distances = []
for hold in range(0,time+1):
    distance =(time-hold)*hold
    if distance > race_distance:
        winning_distances.append(distance)
        print(f"time: {time} race distance: {race_distance} hold: {hold} distance: {distance}")
total = len(winning_distances)
print(total)


