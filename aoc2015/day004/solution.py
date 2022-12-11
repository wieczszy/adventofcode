from hashlib import md5


def solve1(inputfile):
    c = 0
    while True:
        h = md5("bgvyzdsv".encode() + str(c).encode())
        if h.hexdigest().startswith("00000"):
            break
        c += 1
    return c


def solve2(inputfile):
    c = 0
    while True:
        h = md5("bgvyzdsv".encode() + str(c).encode())
        if h.hexdigest().startswith("000000"):
            break
        c += 1
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
