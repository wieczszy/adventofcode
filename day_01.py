def calc_fuel(mass):
    return int(mass / 3) - 2

total_fuel = 0

with open('data/day_1.csv', 'r') as f: 
    modules = [int(line) for line in f]

modules_fuel = sum([calc_fuel(module) for module in modules])
print(modules_fuel)

for module in modules:
    base_fuel = calc_fuel(module)
    additional_fuel = 0
    current_fuel = base_fuel

    while True:
        req = calc_fuel(current_fuel)
        if req <= 0 :
            break
        else:
            additional_fuel += req
            current_fuel = req

    total_fuel += base_fuel + additional_fuel

print(total_fuel)