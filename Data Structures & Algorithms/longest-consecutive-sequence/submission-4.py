class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(set(nums))
        res = 0
        curr = 1
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i - 1] + 1:
                    curr += 1
                else:
                    res = max(res, curr)
                    curr = 1
        res = max(res, curr)
        return res