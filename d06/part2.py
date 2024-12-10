import re
from tqdm import tqdm
import copy
from typing import Tuple

def find_guard_in_row(row: list[str]) -> int | None:
    guard_pos = re.search(r"<|>|\^|v", "".join(row))
    return guard_pos.start() if guard_pos else None

def find_guard(matrix: list[list[str]]) -> Tuple[int, int] | None:
    for y, row in enumerate(matrix):
        guard_pos = find_guard_in_row(row)
        if not guard_pos is None:
            return (guard_pos, y)
    return None

def get_guard_direction(matrix: list[list[str]], pos: Tuple[int, int]) -> Tuple[int, int] | None:
    x, y = pos
    match matrix[y][x]:
        case "^":
            return (0, -1)
        case ">":
            return (1, 0)
        case "v":
            return (0, 1)
        case "<":
            return (-1, 0)
    return None

def get_guard_next_rotation(matrix: list[list[str]], pos: Tuple[int, int]) -> Tuple[int, int] | None:
    x, y = pos
    match matrix[y][x]:
        case "<":
            return (0, -1)
        case "^":
            return (1, 0)
        case ">":
            return (0, 1)
        case "v":
            return (-1, 0)
    return None

def next_hop_is_valid(matrix: list[list[str]], pos: Tuple[int, int], direction: Tuple[int, int]) -> bool:
    x, y = pos
    dx, dy = direction
    hx = x + dx
    hy = y + dy

    return (0 <= hx < len(matrix[y]) and 0 <= hy < len(matrix)) and (matrix[hy][hx] != "#")

def get_next_hop(matrix: list[list[str]], pos: Tuple[int, int], direction: Tuple[int, int]) -> str | None:
    x, y = pos
    dx, dy = direction
    hx = x + dx
    hy = y + dy

    return matrix[hy][hx] if (0 <= hx < len(matrix[y]) and 0 <= hy < len(matrix)) else None

def get_next_hop_position(matrix: list[list[str]], pos: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    x, y = pos
    dx, dy = direction
    hx = x + dx
    hy = y + dy

    return (hx, hy) if (0 <= hx < len(matrix[y]) and 0 <= hy < len(matrix)) else (x, y)

def rotate_guard(matrix: list[list[str]], pos: Tuple[int, int]) -> Tuple[int, int] | None:
    x, y = pos
    match matrix[y][x]:
        case "^":
            matrix[y][x] = ">"
        case ">":
            matrix[y][x] = "v"
        case "v":
            matrix[y][x] = "<"
        case "<":
            matrix[y][x] = "^"
    return get_guard_direction(matrix, pos)

def move_guard(matrix: list[list[str]], pos: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    x, y = pos
    dx, dy = direction
    hx = x + dx
    hy = y + dy

    if matrix[hy][hx] == "#":
        return (x, y)

    matrix[hy][hx] = matrix[y][x]
    matrix[y][x] = "X"
    return (hx, hy)

def print_matrix(matrix: list[list[str]]):
    print("\033[H", end="")
    for row in matrix:
        print(" ".join(map(str, row)))
    print(flush=True)

def visit_matrix(matrix: list[list[str]], source: Tuple[int, int]) -> bool:
    guard_position = source
    if not guard_position: return False

    surce_direction = get_guard_direction(matrix, guard_position)
    guard_direction = surce_direction
    if not guard_direction: return False

    visited = set()
    while not (guard_position, guard_direction) in visited:
        if next_hop_is_valid(matrix, guard_position, guard_direction):
            visited.add((guard_position, guard_direction))
            guard_position = move_guard(matrix, guard_position, guard_direction)
            if not guard_position: return False
        elif get_next_hop(matrix, guard_position, guard_direction) == "#":
            guard_direction = rotate_guard(matrix, guard_position)
            if not guard_direction : return False
        else:
            return False
    return True

with open('input.txt') as input_file:
    lines = input_file.read().splitlines()
    matrix = [list(row) for row in lines]

guard_position = find_guard(matrix)
if not guard_position: exit()
gx, gy = guard_position

guard_direction = get_guard_direction(matrix, guard_position)
if not guard_direction: exit()

result = 0
for y, row in enumerate(tqdm(matrix)):
    for x, cel in enumerate(tqdm(row)):
        if matrix[y][x] == "#": continue
        matrix_cp = copy.deepcopy(matrix)
        matrix_cp[y][x] = "#"
        if (visit_matrix(matrix_cp, (gx, gy))):
            result += 1
print(result)
