from math import *

data = [x for x in open('data/day_10.csv', 'r').read().split('\n')]

### PART 1 ###

asteroids = set()
bases = dict()

for i in range(len(data[0])):
    for j in range(len(data)):
        if data[i][j] == '#':
            asteroids.add((j,i))

for asteroid in asteroids:
    seen = set()
    for asteroid2 in asteroids:
        if asteroid != asteroid2:
            angle = atan2(asteroid2[0] - asteroid[0], asteroid[1] - asteroid2[1]) % (2 * pi)
            if angle not in seen:
                if asteroid not in bases.keys():
                    bases[asteroid] = []
                bases[asteroid].append((asteroid2, angle))
                seen.add(angle)

ans = 0
for k,v in bases.items():
    if len(v) > ans:
        ans = len(v)
        coords = k

print(coords, ans)

### PART 2 ###
base = coords
targets = bases[coords]
targets = sorted(targets, key=lambda x: x[1])
t = targets[199][0]
print(t[0] * 100 + t[1])