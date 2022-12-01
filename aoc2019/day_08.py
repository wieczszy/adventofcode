import numpy as np

data = open('data/day_08.csv', 'r').read().strip()
layer_len = 25 * 6
layers = [data[i:i+layer_len] for i in range(0, len(data), layer_len)]
layers = [[int(x) for x in layer] for layer in layers]

### PART 1 ###
C = sorted([[i, layers[i].count(0)] for i in range(len(layers))], key=lambda x: x[1])
r = layers[C[0][0]].count(1) * layers[C[0][0]].count(2)
print(r)

### PART 2 ###
layers = [np.array(layer).reshape((6,25)) for layer in layers]

message = np.zeros((6,25))
message.fill(2)

for i in range(6):
    for j in range(25):
        for layer in layers:
            v = layer[i][j]
            if v == 0 or v == 1:
                message[i][j] = v
                break

for m in message:
    t = [str(int(x)) for x in list(m)]
    print(''.join(t).replace('0',' ').replace('1', '*'))