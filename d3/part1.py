import re

with open('input.txt') as input_file:
    line = input_file.read()
    expressions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)
    expressions = [
        exp.replace("mul(", "").replace(")", "").replace(",", "*")
        for exp in expressions
    ]
    expressions = '+'.join(expressions)
    print(eval(expressions))
