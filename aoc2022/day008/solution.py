def solve1(inputfile):
    grid = []
    visible = 0
    for line in open(inputfile, "r").read().splitlines():
        row = [int(x) for x in line]
        grid.append(row)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or i == len(grid) - 1:
                top, bot, left, right = 1, 1, 1, 1
            elif j == 0 or j == len(grid[i]) - 1:
                top, bot, left, right = 1, 1, 1, 1
            else:
                top, bot, left, right = 0, 0, 0, 0
                d = grid[i][j]
                for x in range(i):
                    if grid[x][j] < d:
                        top = 1
                    else:
                        top = 0
                        break
                for x in range(i + 1, len(grid)):
                    if grid[x][j] < d:
                        bot = 1
                    else:
                        bot = 0
                        break
                for x in range(j):
                    if grid[i][x] < d:
                        left = 1
                    else:
                        left = 0
                        break
                for x in range(j + 1, len(grid[i])):
                    if grid[i][x] < d:
                        right = 1
                    else:
                        right = 0
                        break
            if top + bot + left + right > 0:
                visible += 1

    return visible


def solve2(inputfile):
    grid = []
    ans = 0
    for line in open(inputfile, "r").read().splitlines():
        row = [int(x) for x in line]
        grid.append(row)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            top, bot, left, right = 0, 0, 0, 0
            d = grid[i][j]
            # need to check in reverse, to be middle-out
            for x in range(i - 1, -1, -1):
                top += 1
                if grid[x][j] >= d:
                    break
            for x in range(i + 1, len(grid)):
                bot += 1
                if grid[x][j] >= d:
                    break
            # need to check in reverse, to be middle-out
            for x in range(j - 1, -1, -1):
                left += 1
                if grid[i][x] >= d:
                    break
            for x in range(j + 1, len(grid[i])):
                right += 1
                if grid[i][x] >= d:
                    break

            score = top * bot * left * right
            ans = max(score, ans)

    return ans


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
