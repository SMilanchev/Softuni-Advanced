rows_count = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]

while True:
    tokens = input().split()
    command = tokens[0]
    if command == "END":
        break
    row, col, value = [int(x) for x in tokens[1:]]
    if 0 > col or col >= rows_count or 0 > row or row >= rows_count:
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

[print(" ".join([str(x) for x in el])) for el in matrix]