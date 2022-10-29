# https://www.codewars.com/kata/529bf0e9bdf7657179000008

def valid_rows(sudoku: list[list[int]]) -> bool:
    for row in sudoku:
        if not all(digit in range(0, 10) for digit in row):
            return False
    return True


def valid_columns(sudoku: list[list[int]]) -> bool:
    column_set = set()
    for row in range(9):
        for column in range(9):
            if sudoku[column][row] in column_set:
                return False
            else:
                column_set.add(sudoku[column][row])
        column_set = set()
    return True


def valid_blocks(sudoku: list[list[int]]) -> bool:
    ranges = [range(3), range(3, 6), range(6, 9)]
    blocks = []
    for row in ranges:
        for column in ranges:
            blocks.append([row, column])

    for row_range, column_range in blocks:
        block_set = set()
        for i in row_range:
            for j in column_range:
                if sudoku[i][j] in block_set:
                    return False
                else:
                    block_set.add(sudoku[i][j])
    return True


def valid_solution(sudoku: list[list[int]]) -> bool:
    if valid_rows(sudoku) and valid_columns(sudoku) and valid_blocks(sudoku):
        return True
    return False


correct_solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

incorrect_solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]
]

print(valid_solution(correct_solution))
print(valid_solution(incorrect_solution))
