class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        suffix = [0] * len(nums)
        total = 0
        for i in nums:
            total += i
            prefix.append(total)
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            suffix[i] = total
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        return -1
        