from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)

        for i in range(9):
            row_seen = set()
            col_seen = set()

            for j in range(9):
                square = (i // 3) * 3 + (j // 3)

                val = board[i][j]
                if val != '.':
                    if val in row_seen or val in squares[square]:
                        return False
                    row_seen.add(val)
                    squares[square].add(val)

                col_val = board[j][i]
                if col_val != '.':
                    if col_val in col_seen:
                        return False
                    col_seen.add(col_val)

        return True