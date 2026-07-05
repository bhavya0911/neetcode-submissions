class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        res = []
        for i in strs:
            curr = dict()
            for j in i:
                if j in curr:
                    curr[j] += 1
                else:
                    curr[j] = 1
            res.append(curr)
        i = 0
        done = []
        while i < len(res):
            if not i in done:
                result.append([strs[i]])
                done.append(i)
                j = i + 1
                while j < len(strs):
                    if not j in done:
                        if res[i] == res[j]:
                            result[-1].append(strs[j])
                            done.append(j)
                    j += 1
            i += 1
        return result