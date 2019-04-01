# pylint: disable=missing-docstring

class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self):

        for i,row in enumerate(self.grid):
            col = [row[i] for row in self.grid]

            if len(set(row)) != len(row) or len(set(col)) != len(col):
                return False




        return True

grid = [
    [8,8,4,  1,5,9,  2,2,6],
    [5,2,9,  6,8,2,  8,4,1],
    [6,1,2,  4,2,8,  8,5,9],

    [9,2,8,  8,1,5,  4,6,2],
    [2,5,8,  8,4,6,  1,9,2],
    [4,6,1,  9,2,2,  5,8,8],

    [8,8,6,  2,9,4,  2,1,5],
    [2,4,2,  5,6,1,  9,8,8],
    [1,9,5,  2,8,8,  6,2,4]
]
s = SudokuSolver(grid)
print(s.is_valid())
