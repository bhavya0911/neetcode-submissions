class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        for i in range(length):
            curr = temperatures[i]
            j = i + 1
            while j < length:
                if temperatures[j] > curr:
                    result[i] = j - i
                    break
                j += 1
        return result