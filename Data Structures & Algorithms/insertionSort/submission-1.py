# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if(len(pairs) == 0):
            return []
        result = [copy.deepcopy(pairs)]
        for i in range(1, len(pairs)):
            j = i - 1
            while(j >= 0 and pairs[j + 1].key < pairs[j].key):
                temp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = temp
                j -= 1
            result.append(copy.deepcopy(pairs))
        return result