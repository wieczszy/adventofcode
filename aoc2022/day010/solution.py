def solve1(inputfile):
    X = 1
    C = 0
    H = []
    for line in open(inputfile, "r").read().splitlines():
        C += 1
        if line == "noop":
            H.append((C, X))
        else:
            H.append((C, X))
            C += 1
            H.append((C, X))
            X += int(line.split()[-1])

    H = H[19::40]
    t = sum(x[0] * x[1] for x in H)

    return t


def solve2(inputfile):
    crt = [["  " for _ in range(40)] for _ in range(6)]
    X = 1
    x, y = 0, 0

    for line in open(inputfile, "r").read().splitlines():
        if line == "noop":
            if y >= X - 1 and y <= X + 1:
                crt[x][y] = "▊▊"
            if y == 39:
                x += 1
                y = 0
            else:
                y += 1
        else:
            for _ in range(2):
                if y >= X - 1 and y <= X + 1:
                    crt[x][y] = "▊▊"
                if y == 39:
                    x += 1
                    y = 0
                else:
                    y += 1
            X += int(line.split()[-1])

    for r in crt:
        print("".join(r))

    return 0


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
