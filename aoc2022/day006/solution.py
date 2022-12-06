def solve1(inputfile):
    inn = open(inputfile, "r").read()
    for i in range(len(inn) - 3):
        if len(set(inn[i : i + 4])) == 4:
            r = i + 4
            break
    return r


def solve2(inputfile):
    inn = open(inputfile, "r").read()
    for i in range(len(inn) - 3):
        if len(set(inn[i : i + 14])) == 14:
            r = i + 14
            break
    return r


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
