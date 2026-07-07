class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = []
        res = []
        l = len(nums)
        for i in range(l):
            curr = []
            for j in nums[:i]:
                curr.append(j)
            for j in nums[i+1:]:
                curr.append(j)
            array.append(curr)
        for i in array:
            if i == []:
                return 0
            total = 1
            for j in i:
                total *= j
            res.append(total)
        return res