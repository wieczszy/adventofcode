w1, w2, _ = open('data/day_03.csv', 'r').read().split('\n')'

x_axis = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
y_axis = {'R': 0, 'L': 0, 'U': 1, 'D': -1}

def get_wire_instructions(w):
    return [(x[0], int(x[1:])) for x in w.split(',')]

def get_path(moves):
    x, y = 0, 0
    points = []
    for move in moves:
        for _ in range(move[1]):
            x += x_axis[move[0]]
            y += y_axis[move[0]]
            points.append((x,y))
    return points

def distance(P1, P2):
    return abs(P1[0] - P2[0]) + abs(P1[1] - P2[1])

w1 = get_wire_instructions(w1)
w2 = get_wire_instructions(w2)

P1 = get_path(w1)
P2 = get_path(w2)

C = list(set(P1).intersection(P2))
D = [distance((0,0), c) for c in C]

S = [P1.index(c) + P2.index(c) + 2 for c in C] # add two to compensate for the 0-index

print(min(D))
print(min(S))