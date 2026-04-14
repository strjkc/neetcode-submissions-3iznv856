# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        arr = []
        for i in range(0, len(pairs)):
            subject = pairs[i]
            j = i - 1
            while j >= 0 and pairs[j].key > subject.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = subject
            arr.append(pairs[:])
        return arr

        