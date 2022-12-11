import numpy as np


def solve1(inputfile):
    G = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in open(inputfile, "r").read().splitlines():
        x, y = map(int, line.split("through")[0].split()[-1].split(","))
        _x, _y = map(int, line.split("through")[1].split()[-1].split(","))
        for i in range(x, _x + 1):
            for j in range(y, _y + 1):
                if line.startswith("turn on"):
                    G[i][j] = 1
                elif line.startswith("turn off"):
                    G[i][j] = 0
                else:
                    G[i][j] = 1 if G[i][j] == 0 else 0

    t = sum([sum(g) for g in G])

    return t


def solve2(inputfile):
    G = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in open(inputfile, "r").read().splitlines():
        x, y = map(int, line.split("through")[0].split()[-1].split(","))
        _x, _y = map(int, line.split("through")[1].split()[-1].split(","))
        for i in range(x, _x + 1):
            for j in range(y, _y + 1):
                if line.startswith("turn on"):
                    G[i][j] += 1
                elif line.startswith("turn off"):
                    G[i][j] += -1 if G[i][j] > 0 else 0
                else:
                    G[i][j] += 2

    t = sum([sum(g) for g in G])

    return t


def solve1_numpy(inputfile):
    G = [[0 for _ in range(1000)] for _ in range(1000)]
    G = np.zeros((1000, 1000), "int32")

    for line in open(inputfile, "r").read().splitlines():
        x, y = map(int, line.split("through")[0].split()[-1].split(","))
        _x, _y = map(int, line.split("through")[1].split()[-1].split(","))
        if line.startswith("turn on"):
            G[x : _x + 1, y : _y + 1] = 1
        elif line.startswith("turn off"):
            G[x : _x + 1, y : _y + 1] = 0
        else:
            G[x : _x + 1, y : _y + 1] = np.logical_not(G[x : _x + 1, y : _y + 1])

    t = sum(sum(G))

    return t


def solve2_numpy(inputfile):
    G = [[0 for _ in range(1000)] for _ in range(1000)]
    G = np.zeros((1000, 1000), "int32")

    for line in open(inputfile, "r").read().splitlines():
        x, y = map(int, line.split("through")[0].split()[-1].split(","))
        _x, _y = map(int, line.split("through")[1].split()[-1].split(","))
        if line.startswith("turn on"):
            G[x : _x + 1, y : _y + 1] += 1
        elif line.startswith("turn off"):
            G[x : _x + 1, y : _y + 1] -= 1
            G[G < 0] = 0
        else:
            G[x : _x + 1, y : _y + 1] += 2

    t = sum(sum(G))

    return t


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    # print(solve1(TEST))
    # print(solve2(TEST))

    print("-- SOLUTION --")
    # print(solve1(INPUT))
    print(solve1_numpy(INPUT))
    # print(solve2(INPUT))
    print(solve2_numpy(INPUT))
