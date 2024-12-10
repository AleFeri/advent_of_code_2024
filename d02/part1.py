def is_gradual(series):
    growing = series[0] < series[1]

    for i in range(0, len(series)-1):
        diff = series[i+1] - series[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if not ((growing and diff > 0) or (not growing and diff < 0)):
            return False

    return True


result = 0
with open('input.txt') as input_file:
    result = len([
        line for line in input_file.readlines()
        if is_gradual([int(e) for e in line.split(' ')])
    ])

print(result)
