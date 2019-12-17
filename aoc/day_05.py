from computer import Computer

input_program = [int(x) for x in open('data/day_05.csv', 'r').read().split(',')]

c = Computer(input_program)
while c.state:
    c.compute([1])
print(c.output_value)

c = Computer(input_program)
while c.state:
    c.compute([5])
print(c.output_value)