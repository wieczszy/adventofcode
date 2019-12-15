def search(O, p):
    ans = 0
    for x in O[p]:
        ans += 1
        ans += search(O, x)
    return ans

orbits = open('data/day_06.csv').read().split('\n')
orbits = [o.split(')') for o in orbits]

planets = list(set([x[0] for x in orbits] + [x[1] for x in orbits]))
is_orbited = {}
is_orbiting = {}

for planet in planets:
    is_orbited[planet] = []
    is_orbiting[planet] = []
    for orbit in orbits:
        if orbit[0] == planet:
            is_orbited[planet].append(orbit[1])
        if orbit[1] == planet:
            is_orbiting[planet].append(orbit[0])

A = 0
for planet in planets:
    A += search(is_orbited, planet)

print(A)

sources = set()
destinations = set()

for k in is_orbited.keys():
    sources.add(k)
    for v in is_orbited[k]:
        destinations.add(v)

root = sources.difference(destinations).pop()

c = 'YOU'
p1 = []
while c != root:
    x = is_orbiting[c][0]
    p1.append(x)
    c = x

c = 'SAN'
p2 = []
while c != root:
    x = is_orbiting[c][0]
    p2.append(x)
    c = x

for x in p1:
    if x in p2:
        fca = x
        break

print(p1.index(fca) + p2.index(fca))