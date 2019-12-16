from itertools import permutations

class Computer():
    def __init__(self, program):
        self.state = 1
        self.idx = 0
        self.output_value = None
        self.program = program

    def get_output(self):
         return self.state, self.idx, self.output_value

    def halt(self):
        self.state = 0

    def compute(self, input_value):
        while self.state:
            instruction = str(self.program[self.idx])

            while len(instruction) < 4:
                instruction = '0' + instruction 

            opcode = int(instruction[-2:])
            modes = [int(c) for c in instruction[:-2]][::-1]

            if opcode == 1:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                self.program[pos3] = (pos1 if modes[0] == 1 else self.program[pos1]) + (pos2 if modes[1] == 1 else self.program[pos2])
                self.idx += 4
            elif opcode == 2:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                self.program[pos3] = (pos1 if modes[0] == 1 else self.program[pos1]) * (pos2 if modes[1] == 1 else self.program[pos2])
                self.idx += 4
            elif opcode == 3:
                pos1 = self.program[self.idx+1]
                self.program[pos1] = input_value
                self.idx += 2
            elif opcode == 4:
                pos1 = self.program[self.idx+1]
                self.output_value = self.program[pos1]
                self.idx += 2
                self.get_output()
            elif opcode == 5:
                pos1, pos2 = self.program[self.idx+1], self.program[self.idx+2]
                if (pos1 if modes[0] == 1 else self.program[pos1]):
                    self.idx = (pos2 if modes[1] == 1 else self.program[pos2])
                else:
                    self.idx += 3
            elif opcode == 6:
                pos1, pos2 = self.program[self.idx+1], self.program[self.idx+2]
                if not (pos1 if modes[0] == 1 else self.program[pos1]):
                    self.idx = (pos2 if modes[1] == 1 else self.program[pos2])
                else:
                    self.idx += 3
            elif opcode == 7:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                if (pos1 if modes[0] == 1 else self.program[pos1]) < (pos2 if modes[1] == 1 else self.program[pos2]):
                    self.program[pos3] = 1
                else:
                    self.program[pos3] = 0
                self.idx += 4
            elif opcode == 8:
                pos1, pos2, pos3 = self.program[self.idx+1], self.program[self.idx+2], self.program[self.idx+3]
                if (pos1 if modes[0] == 1 else self.program[pos1]) == (pos2 if modes[1] == 1 else self.program[pos2]):
                    self.program[pos3] = 1
                else:
                    self.program[pos3] = 0
                self.idx += 4
            else:
                assert opcode == 99
                self.state = 0
                self.get_output()
                break
