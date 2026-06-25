class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return -1
        maxi = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k:
                    maxi = max(maxi, nums[i] + nums[j])
        
        return maxi