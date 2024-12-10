from collections import deque

def pos_is_valid(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

def calc_trailhead_bfs(grid, start_x, start_y):
    x_max, y_max = len(grid), len(grid[0])
    queue = deque([(start_x, start_y, 0)])
    visited = set()
    reachable_nines = set()

    while queue:
        x, y, height = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        current_height = grid[x][y]
        if current_height != height:
            continue

        if current_height == 9:
            reachable_nines.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if pos_is_valid(nx, ny, x_max, y_max) and (nx, ny) not in visited:
                next_height = grid[nx][ny]
                if next_height == current_height + 1:
                    queue.append((nx, ny, next_height))

    return len(reachable_nines)

with open('input.txt') as input_file:
    input_text = input_file.read()

matrix = [list(map(int, line.strip())) for line in input_text.strip().splitlines()]
x_max, y_max = len(matrix), len(matrix[0])
result = 0
for x in range(x_max):
    for y in range(y_max):
        if matrix[x][y] == 0:
            result += calc_trailhead_bfs(matrix, x, y)
print(result)
