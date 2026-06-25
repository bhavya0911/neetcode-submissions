class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dist_for_s = {}
        dist_for_t = {}
        for i in range(len(s)):
            if s[i] in dist_for_s:
                dist_for_s[s[i]] += 1
            else:
                dist_for_s[s[i]] = 1
            if t[i] in dist_for_t:
                dist_for_t[t[i]] += 1
            else:
                dist_for_t[t[i]] = 1
        return dist_for_t == dist_for_s