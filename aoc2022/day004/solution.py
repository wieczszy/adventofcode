def solve1(inputfile):
    t = 0
    for line in open(inputfile, "r").read().splitlines():
        L = line.split(",")
        x, y = list(map(int, L[0].split("-"))), list(map(int, L[1].split("-")))
        if (x[0] >= y[0]) and (x[1] <= y[1]):
            t += 1
        elif (y[0] >= x[0]) and (y[1] <= x[1]):
            t += 1
        else:
            pass
    return t


def solve2(inputfile):
    t = 0
    for line in open(inputfile, "r").read().splitlines():
        L = line.split(",")
        x, y = list(map(int, L[0].split("-"))), list(map(int, L[1].split("-")))
        if set(list(range(x[0], x[1] + 1))) & set(list(range(y[0], y[1] + 1))):
            t += 1
    return t


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
