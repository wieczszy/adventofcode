def solve1(inputfile):
    instructions = open(inputfile, "r").read().splitlines()
    instructions = list(map(lambda x: (x.split()[0], int(x.split()[1])), instructions))

    # starting positions
    # (x, y) on a standard axis statring on (0,0)
    # so y is up/down (change row) and x is left/right (change column)

    t_locations = set()

    H = [0, 0]  # (row, column)
    T = [0, 0]

    for step in instructions:
        direction, value = step[0], step[1]

        delta_x = 1 if direction == "R" else -1 if direction == "L" else 0
        delta_y = 1 if direction == "U" else -1 if direction == "D" else 0

        for i in range(value):
            H[0] += delta_x
            H[1] += delta_y

            x_diff = H[0] - T[0]
            y_diff = H[1] - T[1]

            if abs(x_diff) > 1 or abs(y_diff) > 1:
                # if the same column, different row, change row
                if x_diff == 0:
                    T[1] += 1 if y_diff > 0 else -1
                # if different column, the same row, change column
                elif y_diff == 0:
                    T[0] += 1 if x_diff > 0 else -1
                # if different column, different row, move diagonally
                else:
                    T[0] += 1 if x_diff > 0 else -1
                    T[1] += 1 if y_diff > 0 else -1

            t_locations.add(tuple(T))

    return len(t_locations)


def solve2(inputfile):
    instructions = open(inputfile, "r").read().splitlines()
    instructions = list(map(lambda x: (x.split()[0], int(x.split()[1])), instructions))

    t_locations = set()

    K = [[0, 0] for _ in range(10)]

    for step in instructions:
        direction, value = step[0], step[1]

        delta_x = 1 if direction == "R" else -1 if direction == "L" else 0
        delta_y = 1 if direction == "U" else -1 if direction == "D" else 0

        for i in range(value):
            K[0][0] += delta_x
            K[0][1] += delta_y

            for k in range(1, len(K)):
                H = K[k - 1]
                T = K[k]

                x_diff = H[0] - T[0]
                y_diff = H[1] - T[1]

                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    # if the same column, different row, change row
                    if x_diff == 0:
                        T[1] += 1 if y_diff > 0 else -1
                    # if different column, the same row, change column
                    elif y_diff == 0:
                        T[0] += 1 if x_diff > 0 else -1
                    # if different column, different row, move diagonally
                    else:
                        T[0] += 1 if x_diff > 0 else -1
                        T[1] += 1 if y_diff > 0 else -1

            t_locations.add(tuple(K[-1]))

    return len(t_locations)


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"
    TEST2 = "test2.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
