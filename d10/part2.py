def pos_is_valid(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

def find_distinct_paths(grid, x, y, current_path):
    x_max, y_max = len(grid), len(grid[0])
    if grid[x][y] == 9:
        return {tuple(current_path)}

    paths = set()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if pos_is_valid(nx, ny, x_max, y_max):
            if grid[nx][ny] == grid[x][y] + 1:
                paths |= find_distinct_paths(grid, nx, ny, current_path + [(nx, ny)])
    return paths

def calc_trailhead_rating(grid, start_x, start_y):
    return len(find_distinct_paths(grid, start_x, start_y, [(start_x, start_y)]))

with open('input.txt') as input_file:
    input_text = input_file.read()

matrix = [
    [int(char) if char.isdigit() else -1 for char in line.strip()]
    for line in input_text.strip().splitlines()
]
x_max, y_max = len(matrix), len(matrix[0])

total_rating = 0
for x in range(x_max):
    for y in range(y_max):
        if matrix[x][y] == 0:
            total_rating += calc_trailhead_rating(matrix, x, y)

print(total_rating)
