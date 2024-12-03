import re

with open('input.txt') as input_file:
    line = input_file.read()
    expressions = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))", line)
    expressions = [val for tup in expressions for val in tup if val]

    possible = True
    actual_expressions = []
    for i in range(0, len(expressions)):
        exp = expressions[i]
        if exp == "don't()":
            possible = False
        elif exp == "do()":
            possible = True
        elif possible:
            actual_expressions.append(exp)

    expressions = [
        exp.replace("mul(", "").replace(")", "").replace(",", "*")
        for exp in actual_expressions
    ]
    expressions = '+'.join(expressions)
    print(eval(expressions) if expressions else 0)
