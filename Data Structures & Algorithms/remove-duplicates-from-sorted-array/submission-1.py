class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)