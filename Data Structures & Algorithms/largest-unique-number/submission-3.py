class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        setting = set()
        mapping = {}
        for i in nums:
            setting.add(i)
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
        setting = sorted(list(setting))
        for i in range(len(setting) - 1, -1, -1):
            if mapping[setting[i]] == 1:
                return setting[i]
        return -1