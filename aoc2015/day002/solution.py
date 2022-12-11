def solve1(inputfile):
    t = 0
    for line in open(inputfile, "r").read().splitlines():
        l, w, h = map(int, line.split("x"))
        t += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
    return t


def solve2(inputfile):
    t = 0
    for line in open(inputfile, "r").read().splitlines():
        d1, d2, d3 = sorted(map(int, line.split("x")))
        t += d1 + d1 + d2 + d2 + d1 * d2 * d3
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
