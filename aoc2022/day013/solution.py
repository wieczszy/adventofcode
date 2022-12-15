def compare(x, y):
    if type(x) == int and type(y) == int:
        if x < y:
            return 1
        elif x > y:
            return -1
        else:
            return 0
    elif type(x) == int and type(y) == list:
        return compare([x], y)
    elif type(x) == list and type(y) == int:
        return compare(x, [y])
    else:
        for _x, _y in zip(x, y):
            r = compare(_x, _y)
            if r:
                return r
        if len(x) < len(y):
            return 1
        if len(x) == len(y):
            return 0
        else:
            return -1


def solve1(inputfile):
    packets = [eval(x) for x in open(inputfile, "r").read().splitlines() if x != ""]
    ans = 0
    for i, pair in enumerate(list(zip(packets[0::2], packets[1::2]))):
        x, y = pair[0], pair[1]
        if compare(x, y) == 1:
            ans += i + 1
    return ans


def solve2(inputfile):
    packets = [eval(x) for x in open(inputfile, "r").read().splitlines() if x != ""]
    idx2, idx6 = 1, 2
    for p in packets:
        if compare(p, [[2]]) == 1:
            idx2 += 1
            idx6 += 1
        elif compare(p, [[6]]) == 1:
            idx6 += 1
        else:
            pass
    return idx2 * idx6


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
