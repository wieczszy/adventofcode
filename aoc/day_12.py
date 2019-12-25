import numpy as np
from itertools import combinations

moons = {
    'Io': {'pos':[16, -8, 13], 'vel':[0, 0, 0]},
    'Europa': {'pos':[4, 10, 10], 'vel':[0, 0, 0]},
    'Ganymede': {'pos':[17, -5, 6], 'vel':[0, 0, 0]},
    'Callisto': {'pos':[13, -3, 0], 'vel':[0, 0, 0]}
}

for n in range(1000):

    for p in combinations(moons.keys(), 2):
        for i in range(3):
            if moons[p[0]]['pos'][i] > moons[p[1]]['pos'][i]:
                moons[p[0]]['vel'][i] -= 1
                moons[p[1]]['vel'][i] += 1
            elif moons[p[0]]['pos'][i] < moons[p[1]]['pos'][i]:
                moons[p[0]]['vel'][i] += 1
                moons[p[1]]['vel'][i] -= 1
            else:
                assert moons[p[0]]['pos'][i] == moons[p[1]]['pos'][i]
                pass

    for k in moons.keys():
        for i in range(3):
            moons[k]['pos'][i] += moons[k]['vel'][i]
        
total_energy = 0
for k in moons.keys():
    pot, kin = 0, 0
    for i in range(3):
        pot += abs(moons[k]['pos'][i])
        kin += abs(moons[k]['vel'][i])
    total_energy += pot * kin

print(total_energy)
