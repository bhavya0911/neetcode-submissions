class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)
        rows = []
        columns = []
        squares = []
        for i in range(l):
            rows.append(defaultdict(int))
            columns.append(defaultdict(int))
            squares.append(defaultdict(int))
        for i in range(l):
            for j in range(l):
                curr = board[i][j]
                if curr != ".":
                    rows[i][curr] += 1
                    if rows[i][curr] > 1:
                        return False
                    columns[j][curr] += 1
                    if columns[j][curr] > 1:
                        print("columns")
                        return False
                    square_number = int((i // 3) * 3) + int(j // 3)
                    squares[square_number][curr] += 1
                    if squares[square_number][curr] > 1:
                        print("square")
                        return False
        return True