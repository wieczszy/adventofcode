from itertools import permutations
from computer import Computer

### INPUT ###
program = [int(x) for x in open('data/day_07.csv', 'r').read().split(',')]

### PART 1 ###
settings = permutations([i for i in range(5)], 5)
R = 0
for s in settings:
    c = Computer(program)
    tmp = c.compute([s[0], 0])
    for i in range(1,5):
        c = Computer(program)
        tmp = c.compute([s[i], tmp])
    if tmp > R:
        R = tmp
    
print(R)

### PART 2 ###
settings = permutations([i for i in range(5,10)], 5)
R = 0

for s in settings:
    computers = [Computer(program) for i in range(5)]
    values = [0] * len(computers)
    for i in range(len(computers)):
        _ = computers[i].compute([s[i]])
    while computers[-1].state:
        values[1] = computers[0].compute([values[0]])
        values[2] = computers[1].compute([values[1]])
        values[3] = computers[2].compute([values[2]])
        values[4] = computers[3].compute([values[3]])
        values[0] = computers[4].compute([values[4]])
    if computers[-1].get_output() > R:
        R = computers[-1].get_output()

print(R)
