def solve1(inputfile):
    inn = open(inputfile, 'r').read()
    I = [x.split('\n') for x in inn.split('\n\n')]
    I = [sum([int(y) for y in x]) for x in I]

    return max(I)

def solve2(inputfile):
    inn = open(inputfile, 'r').read()
    I = [x.split('\n') for x in inn.split('\n\n')]
    I = [sum([int(y) for y in x]) for x in I]

    return sum(sorted(I)[-3:])

if __name__ == '__main__':
    TEST = 'test.txt'
    INPUT = 'input.txt'

    print('-- TEST --')
    print(solve1(TEST))
    print(solve2(TEST))

    print('-- SOLUTION --')
    print(solve1(INPUT))
    print(solve2(INPUT))
