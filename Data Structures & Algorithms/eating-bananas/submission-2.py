import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            ho = self.cal(piles, mid)
            if ho <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def cal(self, piles: List[int], k: int) -> int:
        sum = 0
        for i in piles:
            sum += math.ceil(i / k)
        return sum