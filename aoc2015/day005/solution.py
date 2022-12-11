import re


def solve1(inputfile):
    t = 0
    for line in open(inputfile, "r").read().splitlines():
        if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
            pass
        elif len([c for c in line if c in "aeiou"]) >= 3:
            for i in range(len(line) - 1):
                if line[i] == line[i + 1]:
                    t += 1
                    break
        else:
            pass
    return t


def solve2(inputfile):
    t = 0
    for line in open(inputfile, "r").read().splitlines():
        c1, c2 = 0, 0
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                c1 = 1
                break
        for i in range(len(line) - 1):
            pair = line[i : i + 2]
            if len(re.findall(pair, line)) >= 2:
                c2 = 1
                break
        if c1 > 0 and c2 > 0:
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
