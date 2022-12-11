def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def solve1(inputfile):
    M = {}
    inn = open(inputfile, "r").read()
    inn = [x.split("\n") for x in inn.split("\n\n")]

    for item in inn:
        m = item[0].lower().replace(":", "")
        M[m] = {
            "items": [int(y) for y in item[1].split(":")[1].split(",")],
            "operation": eval("lambda old:" + item[2].split("=")[1]),
            "divisible_by": int(item[3].split()[-1]),
            "if_true": " ".join(item[4].split()[-2:]),
            "if_false": " ".join(item[5].split()[-2:]),
            "inspections": 0,
        }

    for _ in range(20):
        for m in M:
            for item in M[m]["items"]:
                item = M[m]["operation"](item)
                item = item // 3
                if item % M[m]["divisible_by"] == 0:
                    M[M[m]["if_true"]]["items"].append(item)
                else:
                    M[M[m]["if_false"]]["items"].append(item)
                M[m]["inspections"] += 1
            M[m]["items"] = []

    X = sorted([M[m]["inspections"] for m in M])[-2:]

    return X[0] * X[1]


def solve2(inputfile):
    M = {}
    inn = open(inputfile, "r").read()
    inn = [x.split("\n") for x in inn.split("\n\n")]

    for item in inn:
        m = item[0].lower().replace(":", "")
        M[m] = {
            "items": [int(y) for y in item[1].split(":")[1].split(",")],
            "operation": eval("lambda old:" + item[2].split("=")[1]),
            "divisible_by": int(item[3].split()[-1]),
            "if_true": " ".join(item[4].split()[-2:]),
            "if_false": " ".join(item[5].split()[-2:]),
            "inspections": 0,
        }

    fac = 1
    for m in M:
        fac *= M[m]["divisible_by"]

    for _ in range(10000):
        for m in M:
            for item in M[m]["items"]:
                item = M[m]["operation"](item)
                item = item % fac
                if item % M[m]["divisible_by"] == 0:
                    M[M[m]["if_true"]]["items"].append(item)
                else:
                    M[M[m]["if_false"]]["items"].append(item)
                M[m]["inspections"] += 1
            M[m]["items"] = []

    X = sorted([M[m]["inspections"] for m in M])[-2:]

    return X[0] * X[1]


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
