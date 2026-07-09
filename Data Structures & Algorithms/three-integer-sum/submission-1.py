class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            curr = nums[i]
            if i == 1:
                print(curr)
            l = 0
            r = len(nums) - 1
            tar = []
            while l < r and (l < i) and (r > i):
                curr_in = nums[l] + nums[r]
                if curr + curr_in > 0:
                    r -= 1
                elif curr + curr_in < 0:
                    l += 1
                else:
                    tar.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            if tar != []:
                for j in tar:
                    a = sorted([curr, j[0], j[1]])
                    if a not in res:
                        res.append(a)
        return res