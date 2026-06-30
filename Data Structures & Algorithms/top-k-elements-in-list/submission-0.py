class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for i in nums:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        ans = list({k: v for k, v in sorted(result.items(), key=lambda item: item[1])})
        start = len(result.keys()) - k
        result1 = []
        for start in range(start, len(result.keys())):
            result1.append(ans[start])
        return result1