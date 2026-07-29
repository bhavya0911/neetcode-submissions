class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0
        l = 0
        currLength = 0
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            currLength += 1
            while target <= currSum:
                if res == 0:
                    res = currLength
                res = min(res, currLength)
                currSum -= nums[l]
                l += 1
                currLength -= 1
        return res