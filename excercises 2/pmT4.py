def print_matrix(matrix, rows_to_print):
    for row in matrix[:rows_to_print]:
        print(' '.join(row))

def create_matrix(n):
    return [['.' for _ in range(n)] for _ in range(1000)]

def main():
    n = int(input())
    matrix = create_matrix(n)
    row, col = 0, 0
    matrix[row][col] = '*'
    last_row_with_asterisk = 0

    while True:
        move = input()
        if move == "END":
            break

        for direction in move:
            if direction == 'R':
                if col < n - 1:
                    col += 1
            elif direction == 'L':
                if col > 0:
                    col -= 1
            elif direction == 'B':
                row += 1

            matrix[row][col] = '*'
            last_row_with_asterisk = max(last_row_with_asterisk, row)

    rows_to_print = last_row_with_asterisk + 1 if last_row_with_asterisk > 0 else 1
    print_matrix(matrix, rows_to_print)

    # Checking the position of the last asterisk
    if col != n - 1:
        print("There's no way out!")

if __name__ == "__main__":
    main()
