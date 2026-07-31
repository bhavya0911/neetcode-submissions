class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for i in matrix:
            prefix = []
            total = 0
            for j in i:
                total += j
                prefix.append(total)
            self.prefix.append(prefix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            right = self.prefix[i][col2]
            left = self.prefix[i][col1 - 1] if col1 > 0 else 0
            sum = right - left
            ans += sum
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)