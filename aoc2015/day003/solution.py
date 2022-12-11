def solve1(inputfile):
    L = set((0, 0))
    x, y = 0, 0
    for c in open(inputfile, "r").read():
        dx = 1 if c == ">" else -1 if c == "<" else 0
        dy = 1 if c == "^" else -1 if c == "v" else 0
        x += dx
        y += dy
        L.add((x, y))
    return len(L)


def solve2(inputfile):
    L = set((0, 0))
    for i in range(2):
        x, y = 0, 0
        for c in open(inputfile, "r").read()[i::2]:
            dx = 1 if c == ">" else -1 if c == "<" else 0
            dy = 1 if c == "^" else -1 if c == "v" else 0
            x += dx
            y += dy
            L.add((x, y))
    return len(L) - 1


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
