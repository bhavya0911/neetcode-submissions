class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outL, outR = 0, len(matrix) - 1
        while outL <= outR:
            mid = (outL + outR) // 2
            if target < matrix[mid][-1]:
                if target > matrix[mid][0]:
                    curr = matrix[mid]
                    l, r = 0, len(curr) - 1
                    while l <= r:
                        middle = (l + r) // 2
                        if target < curr[middle]:
                            r = middle - 1
                        elif target > curr[middle]:
                            l = middle + 1
                        else:
                            return True
                    return False
                elif target < matrix[mid][0]:
                    outR = mid - 1
                else:
                    return True
            elif target > matrix[mid][-1]:
                outL = mid + 1
            else:
                return True
        return False