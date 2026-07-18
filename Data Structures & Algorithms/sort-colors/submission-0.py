class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for i in nums:
            counts[i] += 1
        
        counter = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[counter] = i
                counter += 1
        