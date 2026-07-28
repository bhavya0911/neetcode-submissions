class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = []
        res = 0
        l = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                window.pop(0)
                l += 1
            window.append(arr[r])
            curr = sum(window) / len(window)
            if curr >= threshold and len(window) == k:
                res += 1
        return res