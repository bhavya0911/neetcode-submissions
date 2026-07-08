class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    curr = int(board[r][c]) - 1
                    val = 1 << curr
                    square = (r // 3) * 3 + (c // 3)
                    if val & rows[r]:
                        return False
                    if val & cols[c]:
                        return False
                    if val & squares[square]:
                        return False

                    rows[r] |= val
                    cols[c] |= val
                    squares[square] |= val

        return True