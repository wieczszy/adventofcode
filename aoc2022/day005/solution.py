import re


def solve1(inputfile):
    inn = open(inputfile, "r").read()
    inn = inn.split("\n\n")
    S = inn[0].split("\n")
    stacks = {int(x): [] for x in S[-1].split()}
    S.pop()

    for s in S:
        s = (
            s.replace("[", "")
            .replace("]", "")
            .replace(" ", "_")
            .replace("____", "_")
            .split("_")
        )
        for i, x in enumerate(s):
            if x:
                stacks[i + 1].append(x)

    for k, v in stacks.items():
        stacks[k] = v[::-1]

    I = inn[1].split("\n")
    for i in I:
        move = [int(x) for x in re.findall(r"\b\d+\b", i)]
        for i in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

    r = ""
    for k, v in stacks.items():
        r += v[-1]

    return r


def solve2(inputfile):
    inn = open(inputfile, "r").read()
    inn = inn.split("\n\n")
    S = inn[0].split("\n")
    stacks = {int(x): [] for x in S[-1].split()}
    S.pop()

    for s in S:
        s = (
            s.replace("[", "")
            .replace("]", "")
            .replace(" ", "_")
            .replace("____", "_")
            .split("_")
        )
        for i, x in enumerate(s):
            if x:
                stacks[i + 1].append(x)

    for k, v in stacks.items():
        stacks[k] = v[::-1]

    I = inn[1].split("\n")
    for i in I:
        move = [int(x) for x in re.findall(r"\b\d+\b", i)]
        topop = stacks[move[1]][-move[0] :]
        for p in topop:
            stacks[move[2]].append(p)
            stacks[move[1]].pop()

    r = ""
    for k, v in stacks.items():
        r += v[-1]

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
