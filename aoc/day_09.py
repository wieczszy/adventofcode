from computer import Computer

program = [int(x) for x in open('data/day_09.csv', 'r').read().split(',')]

### PART 1 ###
c = Computer(program)
while c.state:
    c.compute([1], debug=False)
print(c.output_value)

### PART 2 ###
c = Computer(program)
while c.state:
    c.compute([2], debug=False)
print(c.output_value)