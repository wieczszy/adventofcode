def solve1(inputfile):
    ans = 0
    for c in open(inputfile, "r").read():
        ans += 1 if c == "(" else -1
    return ans


def solve2(inputfile):
    ans, c = 0, 0
    for i, c in enumerate(open(inputfile, "r").read()):
        ans += 1 if c == "(" else -1
        if ans == -1:
            c = i + 1
            break
    return c


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
