def count_xmas(grid):
    width, height = len(grid[0]), len(grid)
    xmas = "XMAS"
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    count = 0

    for y in range(height):
        for x in range(width):

            # Any character other "X" is an easy indicator to just keep searching
            if grid[y][x] != "X":
                continue

            for dy, dx in directions:
                found = True
                for i in range(4):
                    new_y = y + dy * i
                    new_x = x + dx * i
                    if not (0 <= new_y < height and 0 <= new_x < width and grid[new_y][new_x] == xmas[i]):
                        found = False
                        break
                if found:
                    count += 1
    return count

def count_x_mas_shapes(grid):
    width, height = len(grid[0]), len(grid)
    count = 0

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if grid[y][x] != "A":
                continue

            diagonal_1 = grid[y - 1][x - 1] + "A" + grid[y + 1][x + 1]
            diagonal_2 = grid[y - 1][x + 1] + "A" + grid[y + 1][x - 1]

            # both diagonals must form "MAS" or "SAM" shape to be considered valid
            if diagonal_1 in ("MAS", "SAM") and diagonal_2 in ("MAS", "SAM"):
                count += 1

    return count

with open("day_4_input.txt") as f:
    grid = [line.strip() for line in f if line.strip()]

print("Part 1 answer:", count_xmas(grid)) # 2397
print("Part 2 answer:", count_x_mas_shapes(grid)) # 1824
