# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0)

    def mergeSortHelper(self, arr: List[Pair], levels: int) -> List[Pair]:
        if len(arr) <= 1:
            return arr
        
        mid = int(len(arr) / 2)
        first = self.mergeSortHelper(arr[:mid], levels + 1)
        second = self.mergeSortHelper(arr[mid:], levels + 1)
        return self.merge(first, second)

    def merge(self, first: List[Pair], second: List[Pair]) -> List[Pair]:
        result = []
        f  = s = 0

        while f < len(first) and s < len(second):
            if first[f].key <= second[s].key:
                result.append(first[f])
                f += 1
            else:
                result.append(second[s])
                s += 1

        while f < len(first):
            result.append(first[f])
            f += 1

        while s < len(second):
            result.append(second[s])
            s += 1

        return result