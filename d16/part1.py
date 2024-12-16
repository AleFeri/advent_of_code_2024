from queue import PriorityQueue

def parse_map(input_map):
    grid = [list(row) for row in input_map.strip().split('\n')]
    return grid

def find_char_pos(grid, nidle):
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == nidle:
                return (x, y)
    return None

def get_neighbors_with_directions(grid, node, direction):
    rows, cols = len(grid), len(grid[0])
    x, y = node
    directions = {
        'north': (0, -1),
        'east': (1, 0),
        'south': (0, 1),
        'west': (-1, 0)
    }
    neighbors = []

    for dir_name, (dx, dy) in directions.items():
        nx, ny = x + dx, y + dy
        if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] in ('.', 'S', 'E'):
            neighbors.append(((nx, ny), dir_name))

    return neighbors

def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def direction_change_cost(current_direction, new_direction):
    directions = ['north', 'east', 'south', 'west']
    current_idx = directions.index(current_direction)
    new_idx = directions.index(new_direction)
    return min(abs(current_idx - new_idx), 4 - abs(current_idx - new_idx)) * 1000

def a_star_with_turn_cost(grid, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start, 'east'))
    came_from = {}
    g_score = {(start, 'east'): 0}
    f_score = {(start, 'east'): heuristic(start, goal)}
    visited = set()

    while not open_set.empty():
        _, current_node, current_direction = open_set.get()

        if (current_node, current_direction) in visited:
            continue
        visited.add((current_node, current_direction))

        if current_node == goal:
            path = reconstruct_path(came_from, (current_node, current_direction))
            return g_score[(current_node, current_direction)], path

        for neighbor, new_direction in get_neighbors_with_directions(grid, current_node, current_direction):
            movement_cost = 1
            rotation_cost = direction_change_cost(current_direction, new_direction)

            tentative_g_score = g_score[(current_node, current_direction)] + movement_cost + rotation_cost

            if (neighbor, new_direction) not in g_score or tentative_g_score < g_score[(neighbor, new_direction)]:
                came_from[(neighbor, new_direction)] = (current_node, current_direction)
                g_score[(neighbor, new_direction)] = tentative_g_score
                f_score[(neighbor, new_direction)] = tentative_g_score + heuristic(neighbor, goal)
                open_set.put((f_score[(neighbor, new_direction)], neighbor, new_direction))

    return None, []

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current[0])
        current = came_from[current]
    path.reverse()
    return path

with open("input.txt", 'r') as file:
    input_map = file.read()

grid = parse_map(input_map)
start = find_char_pos(grid, 'S')
goal = find_char_pos(grid, 'E')

cost, path = a_star_with_turn_cost(grid, start, goal)

print(cost)
