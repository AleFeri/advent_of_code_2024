from typing import Tuple
from itertools import product

def evaluate(numbers: list[int], operators: Tuple[str, ...]) -> int:
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

with open('input.txt') as input_file:
    lines = input_file.read().splitlines()

result = 0
for line in lines:
    aspected_result, operands = line.split(": ")
    aspected_result = int(aspected_result)
    operands = list(map(int, operands.split()))
    operations = product("+*", repeat=len(operands)-1)

    for op in operations:
        if evaluate(operands, op) == aspected_result:
            result += aspected_result
            break

print(result)
