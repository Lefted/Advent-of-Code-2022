# Change directory to the directory of this file
import re
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read input
with open('input.txt') as file:
    input = file.read()

# Define variables
monkeys = []
for i in range(8):
    monkeys.append({'items': []})
    # set number_of_times_inspected to 0
    monkeys[i]['number_of_times_inspected'] = 0

# Parse input
regex = re.compile(r'Monkey (\d):(.+?)\n\n', re.DOTALL)
monkey_sections = regex.findall(input)
for monkey_section in monkey_sections:
    # regex to get monkey number
    monkey_number = int(monkey_section[0])
    # regex to get starting items which has the form 'Starting items:
    regex = re.compile(r'Starting items: (.+?)\n', re.DOTALL)
    starting_items = regex.findall(monkey_section[1])[0].split(', ')

    # regex to get the test condition which has the form 'Operation: new = old +/* number/old'
    regex = re.compile(r'Operation: new = old (\+|\*) (\d+|old)')
    operation = regex.findall(monkey_section[1])[0]

    regex = re.compile(r'Test: divisible by (\d+)')
    test_condition = regex.findall(monkey_section[1])[0]

    # regex to get the test case and the monkey to throw to where the pattern is 'If true: throw to monkey (\d+)' or 'If false: throw to monkey (\d+).'
    regex = re.compile(r'If (true|false): throw to monkey (\d+)')
    test_cases = regex.findall(monkey_section[1])

    # assign everything to the monkey
    print(monkey_number)
    monkeys[monkey_number]['test_condition'] = int(test_condition)
    monkeys[monkey_number]['test_cases'] = test_cases
    monkeys[monkey_number]['operation'] = operation
    for item in starting_items:
        monkeys[monkey_number]['items'].append(int(item))

for monkey in monkeys:
    print(monkey)


# Chinese remainder theorem
big_mod = 1
for monkey in monkeys:
    big_mod *= monkey['test_condition']
    print(big_mod)


def execute_operation(operation, old):
    if operation[0] == '+':
        if operation[1] == 'old':
            ans = old << 1
        else:
            ans = old + int(operation[1])
    elif operation[0] == '*':
        if operation[1] == 'old':
            ans = old ** 2
        else:
            ans = old * int(operation[1])
    return ans % big_mod


def test_condition(test_condition, new):
    if new % int(test_condition) == 0:
        return True
    else:
        return False


def throw_item(monkey_number, monkey_to_throw_to, new):
    monkeys[monkey_to_throw_to]['items'].append(new)


def inspect_item(monkey_number, item):
    operation = monkeys[monkey_number]['operation']
    condition = monkeys[monkey_number]['test_condition']
    cases = monkeys[monkey_number]['test_cases']

    new = execute_operation(operation, item)

    if test_condition(condition, new):
        monkey_to_throw_to = int(cases[0][1])
    else:
        monkey_to_throw_to = int(cases[1][1])
    throw_item(monkey_number, monkey_to_throw_to, new)

    # increase number of times monkey has inspected an item
    monkeys[monkey_number]['number_of_times_inspected'] += 1


# Run simulation
for i in range(10_000):
    for monkey_number, monkey in enumerate(monkeys):
        # iterate while popping the items
        while monkey['items']:
            item = monkey['items'].pop(0)
            inspect_item(monkey_number, item)


def calculate_level_of_monkey_business(monkeys):
    # get the two most active monkeys
    most_active_monkeys = sorted(
        monkeys, key=lambda monkey: monkey['number_of_times_inspected'], reverse=True)[:2]
    # multiply the number of items inspected by each monkey
    level_of_monkey_business = most_active_monkeys[0]['number_of_times_inspected'] * \
        most_active_monkeys[1]['number_of_times_inspected']
    return level_of_monkey_business


print(calculate_level_of_monkey_business(monkeys))
