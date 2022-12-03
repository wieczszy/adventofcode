def solve1(inputfile):
    t = 0
    for line in open(inputfile, "r").read().splitlines():
        p1, p2 = line[: len(line) / 2], line[len(line) / 2 :]
        for x in list(set(p1).intersection(p2)):
            if x.islower():
                t += ord(x) - ord('a') + 1
            else:
                t += ord(x) - ord('A') + 27
    return t


def solve2(inputfile):
    t = 0
    inn = open(inputfile, "r").read().splitlines()
    for i in range(0, len(inn), 3):
        g = inn[i : i + 3]
        x, = set(g[0]).intersection(g[1], g[2])
        if x.islower():
            t += ord(x) - ord('a') + 1
        else:
            t += ord(x) - ord('A') + 27
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
