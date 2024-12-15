def dfs(r, c, plant_type):
    stack = [(r, c)]
    area = 0
    perimeter = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        area += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if garden_map[nx][ny] == plant_type and not visited[nx][ny]:
                    stack.append((nx, ny))
                elif garden_map[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1
    return area, perimeter

with open("input.txt", 'r') as file:
    garden_map = [line.strip() for line in file.readlines()]

rows, cols = len(garden_map), len(garden_map[0])
visited = [[False] * cols for _ in range(rows)]

total_price = 0
for r in range(rows):
    for c in range(cols):
        if not visited[r][c]:
            plant_type = garden_map[r][c]
            area, perimeter = dfs(r, c, plant_type)
            total_price += area * perimeter

print(total_price)
