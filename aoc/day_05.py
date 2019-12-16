def compute(input_program, input_value):
    program = input_program.copy()
    i = 0
    r = []
    while True:
        instruction = str(program[i])

        while len(instruction) < 4:
            instruction = '0' + instruction 

        opcode = int(instruction[-2:])
        modes = [int(c) for c in instruction[:-2]][::-1]

        if opcode == 1:
            pos1, pos2, pos3 = program[i+1], program[i+2], program[i+3]
            program[pos3] = (pos1 if modes[0] == 1 else program[pos1]) + (pos2 if modes[1] == 1 else program[pos2])
            i += 4
        elif opcode == 2:
            pos1, pos2, pos3 = program[i+1], program[i+2], program[i+3]
            program[pos3] = (pos1 if modes[0] == 1 else program[pos1]) * (pos2 if modes[1] == 1 else program[pos2])
            i += 4
        elif opcode == 3:
            pos1 = program[i+1]
            program[pos1] = input_value
            i += 2
        elif opcode == 4:
            pos1 = program[i+1]
            r.append(program[pos1])
            i += 2
        elif opcode == 5:
            pos1, pos2 = program[i+1], program[i+2]
            if (pos1 if modes[0] == 1 else program[pos1]):
                i = (pos2 if modes[1] == 1 else program[pos2])
            else:
                i += 3
        elif opcode == 6:
            pos1, pos2 = program[i+1], program[i+2]
            if not (pos1 if modes[0] == 1 else program[pos1]):
                i = (pos2 if modes[1] == 1 else program[pos2])
            else:
                i += 3
        elif opcode == 7:
            pos1, pos2, pos3 = program[i+1], program[i+2], program[i+3]
            if (pos1 if modes[0] == 1 else program[pos1]) < (pos2 if modes[1] == 1 else program[pos2]):
                program[pos3] = 1
            else:
                program[pos3] = 0
            i += 4
        elif opcode == 8:
            pos1, pos2, pos3 = program[i+1], program[i+2], program[i+3]
            if (pos1 if modes[0] == 1 else program[pos1]) == (pos2 if modes[1] == 1 else program[pos2]):
                program[pos3] = 1
            else:
                program[pos3] = 0
            i += 4
        else:
            assert opcode == 99
            break

    return r[-1]

input_program = [int(x) for x in open('data/day_05.csv', 'r').read().split(',')]

print(compute(input_program, 1))
print(compute(input_program, 5))