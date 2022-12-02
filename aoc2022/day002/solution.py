def solve1(inputfile):
    score = 0
    bonus = {"X": 1, "Y": 2, "Z": 3}
    result = {
        "A X": 3,
        "B X": 0,
        "C X": 6,
        "A Y": 6,
        "B Y": 3,
        "C Y": 0,
        "A Z": 0,
        "B Z": 6,
        "C Z": 3,
    }

    inn = open(inputfile, "r").readlines()
    inn = [x.strip() for x in inn]

    for r in inn:
        score += bonus[r[2]] + result[r]

    return score


def solve2(inputfile):
    score = 0
    bonus = {"A": 1, "B": 2, "C": 3}
    shape = {
        "A X": "C",
        "B X": "A",
        "C X": "B",
        "A Y": "A",
        "B Y": "B",
        "C Y": "C",
        "A Z": "B",
        "B Z": "C",
        "C Z": "A",
    }
    result = {"X": 0, "Y": 3, "Z": 6}

    inn = open(inputfile, "r").readlines()
    inn = [x.strip() for x in inn]

    for r in inn:
        score += bonus[shape[r]] + result[r[2]]

    return score


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
