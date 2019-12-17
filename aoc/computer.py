class Computer():
    def __init__(self, program):
        self.state = 1
        self.idx = 0
        self.output_value = None
        self.program = program + [0] * 10000
        self.relative_base = 0

    def halt(self):
        self.state = 0

    def get_output(self):
        return self.output_value

    def compute(self, input_value, debug=False):
        while self.state:
            instruction = str(self.program[self.idx])

            while len(instruction) < 5:
                instruction = '0' + instruction 

            opcode = int(instruction[-2:])
            modes = [int(c) for c in instruction[:-2]][::-1]

            if debug:
                print(instruction, opcode, modes, self.output_value)

            if opcode == 1:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                pos2 = (pos2 + self.relative_base if modes[1] == 2 else pos2)
                pos3 = (pos3 + self.relative_base if modes[2] == 2 else pos3)
                self.program[pos3] = (pos1 if modes[0] == 1 else self.program[pos1]) + (pos2 if modes[1] == 1 else self.program[pos2])
                self.idx += 4
            elif opcode == 2:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                pos2 = (pos2 + self.relative_base if modes[1] == 2 else pos2)
                pos3 = (pos3 + self.relative_base if modes[2] == 2 else pos3)
                self.program[pos3] = (pos1 if modes[0] == 1 else self.program[pos1]) * (pos2 if modes[1] == 1 else self.program[pos2])
                self.idx += 4
            elif opcode == 3:
                if input_value == []:
                    break
                pos1 = self.program[self.idx+1]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                self.program[pos1] = input_value[0]
                del input_value[0]
                self.idx += 2
            elif opcode == 4:
                pos1 = self.program[self.idx+1]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                self.output_value = (pos1 if modes[0] == 1 else self.program[pos1])
                self.idx += 2
                break
            elif opcode == 5:
                pos1, pos2 = self.program[self.idx+1], self.program[self.idx+2]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                pos2 = (pos2 + self.relative_base if modes[1] == 2 else pos2)
                if (pos1 if modes[0] == 1 else self.program[pos1]):
                    self.idx = (pos2 if modes[1] == 1 else self.program[pos2])
                else:
                    self.idx += 3
            elif opcode == 6:
                pos1, pos2 = self.program[self.idx+1], self.program[self.idx+2]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                pos2 = (pos2 + self.relative_base if modes[1] == 2 else pos2)
                if not (pos1 if modes[0] == 1 else self.program[pos1]):
                    self.idx = (pos2 if modes[1] == 1 else self.program[pos2])
                else:
                    self.idx += 3
            elif opcode == 7:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                pos2 = (pos2 + self.relative_base if modes[1] == 2 else pos2)
                pos3 = (pos3 + self.relative_base if modes[2] == 2 else pos3)
                if (pos1 if modes[0] == 1 else self.program[pos1]) < (pos2 if modes[1] == 1 else self.program[pos2]):
                    self.program[pos3] = 1
                else:
                    self.program[pos3] = 0
                self.idx += 4
            elif opcode == 8:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                pos2 = (pos2 + self.relative_base if modes[1] == 2 else pos2)
                pos3 = (pos3 + self.relative_base if modes[2] == 2 else pos3)
                if (pos1 if modes[0] == 1 else self.program[pos1]) == (pos2 if modes[1] == 1 else self.program[pos2]):
                    self.program[pos3] = 1
                else:
                    self.program[pos3] = 0
                self.idx += 4
            elif opcode == 9:
                pos1 = self.program[self.idx+1]
                pos1 = (pos1 + self.relative_base if modes[0] == 2 else pos1)
                self.relative_base += (pos1 if modes[0] == 1 else self.program[pos1])
                self.idx += 2
            else:
                assert opcode == 99
                self.state = 0
                break

        return self.output_value