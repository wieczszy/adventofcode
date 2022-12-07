from collections import defaultdict


def get_size1(directory):
    size = 0
    t = 0
    if type(directory) == int:
        return directory, 0
    for subdir in directory.values():
        subsize, subtotal = get_size1(subdir)
        size += subsize
        t += subtotal
    if size <= 100000:
        t += size
    return size, t


def solve1(inputfile):
    cwd = tree = {}
    stack = []
    for line in open(inputfile, "r").read().splitlines():
        if line.startswith("$ cd"):
            current_dir = line.split(" ")[-1]
            if current_dir == "/":
                cwd = tree
                stack = []
            elif current_dir == "..":
                cwd = stack.pop()
            else:
                if current_dir not in cwd:
                    cwd[current_dir] = {}
                stack.append(cwd)
                cwd = cwd[current_dir]
        elif line.startswith("$ ls"):
            pass
        else:
            prop, name = line.split(" ")
            if prop == "dir":
                if name not in cwd:
                    cwd[name] = {}
            else:
                cwd[name] = int(prop)

    _, t = get_size1(tree)

    return t


def get_size2(directory):
    size = 0
    if type(directory) == int:
        return directory
    for subdir in directory.values():
        subsize = get_size2(subdir)
        size += subsize
    return size


def find_delete(directory, space_needed):
    ans = float("inf")
    if get_size2(directory) >= space_needed:
        ans = get_size2(directory)
    for subdir in directory.values():
        if type(subdir) == int:
            continue
        ans = min(ans, find_delete(subdir, space_needed))
    return ans


def solve2(inputfile):
    space_available = 70000000
    space_required = 30000000

    cwd = tree = {}
    stack = []
    for line in open(inputfile, "r").read().splitlines():
        if line.startswith("$ cd"):
            current_dir = line.split(" ")[-1]
            if current_dir == "/":
                cwd = tree
                stack = []
            elif current_dir == "..":
                cwd = stack.pop()
            else:
                if current_dir not in cwd:
                    cwd[current_dir] = {}
                stack.append(cwd)
                cwd = cwd[current_dir]
        elif line.startswith("$ ls"):
            pass
        else:
            prop, name = line.split(" ")
            if prop == "dir":
                if name not in cwd:
                    cwd[name] = {}
            else:
                cwd[name] = int(prop)

    space_taken = get_size2(tree)
    space_free = space_available - space_taken
    space_needed = space_required - space_free

    r = find_delete(tree, space_needed)

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
