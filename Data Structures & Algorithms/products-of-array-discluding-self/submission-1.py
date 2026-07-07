class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        l = len(nums)
        suffix = [0] * l
        prefix = [0] * l
        total = 1
        for i in range(l):
            prefix[i] = total
            total *= nums[i]
        total = 1
        for i in range(l - 1, -1, -1):
            suffix[i] = total
            total *= nums[i]
        for i in range(l):
            res.append(prefix[i] * suffix[i])
        return res