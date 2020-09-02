from collections import deque

rows_count = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]
bombs = deque([[int(m) for m in x.split(",")] for x in input().split()])


def validate_cell(cell_bombed, size, matrix):
    return 0 <= cell_bombed[0] < size and 0 <= cell_bombed[1] < size and matrix[cell_bombed[0]][cell_bombed[1]] > 0


def bomb_action(matrix, row, column):
    r = [-1, -1, -1, 0, 0, 1, 1, 1]
    c = [-1, 0, 1, -1, 1, -1, 0, 1]
    cell_bomb_value = matrix[row][column]
    for i in range(8):
        cell_to_bombed = [r[i] + row, c[i] + column]
        if validate_cell(cell_to_bombed, rows_count, matrix):
            matrix[cell_to_bombed[0]][cell_to_bombed[1]] -= cell_bomb_value
    matrix[row][column] = 0
    return matrix


def solve(matrix, bombs):
    while bombs:
        current_bomb = bombs.popleft()
        bomb_row, bomb_column = current_bomb
        if matrix[bomb_row][bomb_column] > 0:
            bomb_action(matrix, bomb_row, bomb_column)

    return matrix


def print_result(result):
    alive = []
    for el in matrix:
        for i in el:
            if i > 0:
                alive.append(i)
    print(f"Alive cells: {len(alive)}")
    print(f"Sum: {sum(alive)}")
    for el in matrix:
        print(" ".join([str(x) for x in el]))


print_result(solve(matrix, bombs))