from collections import deque


def solve1(inputfile):
    grid = open(inputfile, "r").read().splitlines()

    for x in grid:
        if "E" in x:
            gx, gy = grid.index(x), x.index("E")
        if "S" in x:
            sx, sy = grid.index(x), x.index("S")

    grid = list(
        map(
            lambda C: [
                0 if c == "S" else 25 if c == "E" else ord(c) - ord("a") for c in C
            ],
            grid,
        )
    )

    queue = deque()
    queue.append((0, sx, sy))
    visited = {(sx, sy)}

    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while queue:
        c, i, j = queue.popleft()
        for d in dirs:
            x, y = i + d[0], j + d[1]
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[i]):
                continue
            if grid[x][y] - grid[i][j] > 1:
                continue
            if (x, y) in visited:
                continue
            if (x, y) == (gx, gy):
                ans = c + 1
                break
            visited.add((x, y))
            queue.append((c + 1, x, y))

    return ans


def solve2(inputfile):
    grid = open(inputfile, "r").read().splitlines()

    startpoints = []

    for x in grid:
        if "E" in x:
            gx, gy = grid.index(x), x.index("E")
        for c in x:
            if c == "a":
                sx, sy = grid.index(x), x.index(c)
                startpoints.append((sx, sy))

    grid = list(
        map(
            lambda C: [
                0 if c == "S" else 25 if c == "E" else ord(c) - ord("a") for c in C
            ],
            grid,
        )
    )

    ans = float("inf")

    for point in startpoints:
        sx, sy = point
        queue = deque()
        queue.append((0, sx, sy))
        visited = {(sx, sy)}

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            c, i, j = queue.popleft()
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[i]):
                    continue
                if grid[x][y] - grid[i][j] > 1:
                    continue
                if (x, y) in visited:
                    continue
                if (x, y) == (gx, gy):
                    if c + 1 < ans:
                        ans = c + 1
                    break
                visited.add((x, y))
                queue.append((c + 1, x, y))

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
