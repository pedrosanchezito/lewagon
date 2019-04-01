# pylint: disable=missing-docstring

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def is_valid_row(self):
        columns = []
        for row in self.grid:
            if len(set(row)) != len(row):
                return False

            for col in range(9):
                columns[col].append(row[col])

        for column in columns:
            if len(set(column)) != len(column):
                return False


        return True

grid = [
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [2,3,1, 6,6,4, 8,9,7]
]
s = SudokuSolver(grid)
print(s.is_valid_row())
