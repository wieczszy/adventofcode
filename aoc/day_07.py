from itertools import permutations

def compute(program, input_value, i=0, return_all=False):
    program = input_program.copy()
    r = []
    s = 0
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
            program[pos1] = input_value[0]
            if len(input_value) > 1:
                del input_value[0]
            i += 2
        elif opcode == 4:
            pos1 = program[i+1]
            r.append(program[pos1])
            i += 2
            return program[pos1], s, program, i
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
            s = 1
            break

    if return_all:
        return r, s, program, i

    return r[-1], s, program, i

input_program = [int(x) for x in open('data/day_07.csv', 'r').read().split(',')]
phase_settings = [s for s in permutations([0,1,2,3,4], 5)]

R = 0
for s in phase_settings:
    tmp, _, _, _ = compute(input_program, [s[0], 0])
    for i in range(1,5):
        tmp, _, _, _ = compute(input_program, [s[i], tmp])
    if tmp > R:
        R = tmp

print(R)

##### PART 2 #####

# input_program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# phase_settings = [s for s in permutations([5,6,7,8,9], 5)]

# R = 0

# for s in phase_settings:
#     v0, s0, p0, i0 = compute(input_program, [s[0], 0], return_all=True)
#     v1, s1, p1, i1 = compute(input_program, [s[1], v0], return_all=True)
#     v2, s2, p2, i2 = compute(input_program, [s[2], v1], return_all=True)
#     v3, s3, p3, i3 = compute(input_program, [s[3], v2], return_all=True)
#     v4, s4, p4, i4 = compute(input_program, [s[4], v3], return_all=True)
#     print(i0, i1, i2, i3, i4)
#     print(v0, v1, v2, v3, v4)
#     while True:
#         v0, s0, p0, i0 = compute(p0, [v4], i=i0, return_all=True)
#         v1, s1, p1, i1 = compute(p1, [v0], i=i1, return_all=True)
#         v2, s2, p2, i2 = compute(p2, [v1], i=i2, return_all=True)
#         v3, s3, p3, i3 = compute(p3, [v2], i=i3, return_all=True)
#         v4, s4, p4, i4 = compute(p4, [v3], i=i4, return_all=True)
        
#         if s0 and s1 and s2 and s3 and s4:
#             if v4 < R:
#                 R = v4
#             break