import re
import time
from typing import Tuple

def find_robot_in_row(row: list[str]) -> int | None:
    guard_pos = re.search(r"@", "".join(row))
    return guard_pos.start() if guard_pos else None

def find_robot(matrix: list[list[str]]) -> Tuple[int, int] | None:
    for y, row in enumerate(matrix):
        rx = find_robot_in_row(row)
        if not rx is None:
            return (rx, y)
    return None

def col_to_row(matrix: list[list[str]], col: int) -> list[str]:
    return [row[col] for row in matrix]

def robot_can_exec_command(matrix: list[list[str]], pos: Tuple[int, int], command: str) -> bool:
    x, y = pos

    section = ''
    match command:
        case "^":
            c_t_r = col_to_row(matrix, x)
            section = ''.join(c_t_r[:y][::-1])
        case ">":
            section = ''.join(matrix[y][x:])
        case "v":
            c_t_r = col_to_row(matrix, x)
            section = ''.join(c_t_r[y:])
        case "<":
            section = ''.join(matrix[y][:x][::-1])

    return "." in section and section.index(".") < section.index("#")

def translate_command_to_direction(command: str) -> Tuple[int, int]:
    match command:
        case "^":
            return (0, -1)
        case ">":
            return (1, 0)
        case "v":
            return (0, 1)
        case "<":
            return (-1, 0)
    return (0, 0)

def robot_exec_command(matrix: list[list[str]], pos: Tuple[int, int], command: str) -> list[list[str]]:
    if not robot_can_exec_command(matrix, pos, command):
        return matrix

    x, y = pos
    tx, ty = x, y
    dx, dy = translate_command_to_direction(command)
    match command:
        case "^":
            section = col_to_row(matrix, x)[:y][::-1]
            ty = y - col_to_row(matrix, x)[:y][::-1].index(".") - 1
            for c_y in range(ty, y + 1):
                matrix[c_y][x] = matrix[c_y + (-dy)][x]
        case ">":
            section = matrix[y][x:]
            tx = x + matrix[y][x:].index(".")
            for c_x in range(tx, x, -1):
                matrix[y][c_x] = matrix[y][c_x + (-dx)]
        case "v":
            section = col_to_row(matrix, x)[y:]
            ty = y + col_to_row(matrix, x)[y:].index(".")
            for c_y in range(ty, y, -1):
                matrix[c_y][x] = matrix[c_y + (-dy)][x]
        case "<":
            section = matrix[y][:x][::-1]
            tx = x - matrix[y][:x][::-1].index(".") - 1
            for c_x in range(tx, x+1):
                matrix[y][c_x] = matrix[y][c_x + (-dx)]

    matrix[y][x] = "."

    return matrix

def calculateBoxCoordinates(matrix: list[list[str]]) -> int:
    result = 0
    for y, row in enumerate(matrix):
        for x, elem in enumerate(row):
            if elem == "O":
                result += 100 * y + x
    return result

def print_matrix(matrix: list[list[str]]):
    print("\033[H", end="")
    for row in matrix:
        print(" ".join(map(str, row)))
    print(flush=True)

with open('input.txt') as input_file:
    sections = input_file.read().split("\n\n")
    lines = sections[0].split("\n")
    matrix = [list(row) for row in lines]
    commands = list(sections[1].split("\n"))

r_position = find_robot(matrix)
if not r_position: exit()

for command_set in commands:
    for command in command_set:
        print_matrix(matrix)
        print(f"Robot {r_position[0]}:{r_position[1]} - {command=}")
        matrix = robot_exec_command(matrix, r_position, command)

        r_position = find_robot(matrix)
        if not r_position: exit()

        time.sleep(0.1)

print_matrix(matrix)
print(f"Robot {r_position[0]}:{r_position[1]} - command=' '")

print(calculateBoxCoordinates(matrix))
