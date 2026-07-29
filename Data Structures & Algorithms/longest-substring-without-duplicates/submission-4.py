class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = {}
        res = 0

        for r in range(len(s)): 
            curr = s[r]
            if curr not in window:
                window[curr] = r
            else:
                res = max(res, r - l)
                nex = window[curr]
                while l <= nex:
                    del window[s[l]]
                    l += 1
                window[curr] = r
        if len(window) != 0:
            res = max(res, len(window))
        return res