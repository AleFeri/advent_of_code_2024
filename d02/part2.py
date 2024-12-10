def is_gradual(series):
    if len(series) <= 1: return True

    growing = series[0] < series[1]

    for i in range(0, len(series)-1):
        diff = series[i+1] - series[i]

        if (
            (abs(diff) < 1 or abs(diff) > 3) or
            (not ((growing and diff > 0) or (not growing and diff < 0)))
        ):
            return False

    return True

def is_gradual_with_second_chance(series):
    if is_gradual(series):
        return True

    for i in range(len(series)):
        cleaned_series = series[:i] + series[i + 1:]
        if is_gradual(cleaned_series):
            return True

    return False

result = 0
with open('input.txt') as input_file:
    result = len([
        line for line in input_file.readlines()
        if is_gradual_with_second_chance([int(e) for e in line.split(' ')])
    ])

print(result)
