from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        matrix = [[0 if val == "." else int(val) for val in row] for row in board]

        # Check rows
        for row in matrix:
            counter = Counter(row)
            if 0 in list(counter.keys()):
                counter.pop(0)

            if any(val > 1 for val in counter.values()):
                return False

        # Check columns
        for col in range(9):
            counter = Counter(matrix[row][col] for row in range(9))
            if 0 in list(counter.keys()):
                counter.pop(0)
            

            if any(val > 1 for val in counter.values()):
                return False

        # Check 3 x 3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                counter = Counter(
                    matrix[r][c]
                    for r in range(row, row + 3)
                    for c in range(col, col + 3)
                )
                if 0 in list(counter.keys()):
                    counter.pop(0)

                if any(val > 1 for val in counter.values()):
                    return False

        return True

