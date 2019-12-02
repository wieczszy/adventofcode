def compute(input_program, n, v):
    program = input_program.copy()
    program[1] = n
    program[2] = v
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break
        pos1, pos2, pos3 = program[i+1], program[i+2], program[i+3]
        if opcode == 1:
            program[pos3] = program[pos1] + program[pos2]
        if opcode == 2:
            program[pos3] = program[pos1] * program[pos2]
    return program[0]

with open('data/day_2.csv', 'r') as f:
    base_program = [int(c) for c in f.read().split(',')]

r1 = compute(base_program, 12, 2)

for n in range(100):
    for v in range(100):
        if compute(base_program, n, v) == 19690720:
            r2 = 100 * n + v

print(r1)
print(r2)