class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t = len(nums1) + len(nums2)
        newArray = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                newArray.append(nums1[l])
                l += 1
            else:
                newArray.append(nums2[r])
                r += 1
        while l < len(nums1):
            newArray.append(nums1[l])
            l += 1
        while r < len(nums2):
            newArray.append(nums2[r])
            r += 1

        if t % 2 == 1:
            mid = t // 2
            return float(newArray[mid])
        else:
           index = int(t / 2)
           return float((newArray[index] + newArray[index - 1]) / 2)