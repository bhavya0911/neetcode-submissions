class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for i in nums:
            if i != val:
                result.append(i)
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)