class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = set()

        L = 0
        for R in range(len(nums)):
            if R - L > k:
                l.remove(nums[L])
                L += 1
            if nums[R] in l:
                return True
            l.add(nums[R])

        return False