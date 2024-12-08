import re
from typing import Tuple, Set

def find_antennas_positions(matrix: list[list[str]], antenna: str) -> Set[Tuple[int, int]]:
    positions = set()
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if antenna == col:
                positions.add((x, y))

    return positions

with open('input.txt') as input_file:
    file_text = input_file.read()
    lines = file_text.splitlines()
    antennas = set(re.findall(r"\d+|\w+", file_text))
    matrix = [list(row) for row in lines]

antinodes = set()
for a in antennas:
    positions = find_antennas_positions(matrix, a)
    for current_a in positions:
        antinodes.add(current_a)
        for other_a in positions:
            if current_a == other_a:
                continue
            x, y = current_a
            ox, oy = other_a
            dx, dy = x-ox, y-oy
            px, py = x+dx, y+dy
            while (
                (0 <= px < len(matrix[0]) and 0 <= py < len(matrix))
            ):
                antinodes.add((px, py))
                px += dx
                py += dy
print(len(antinodes))
