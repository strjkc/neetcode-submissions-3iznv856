# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ret = []
        i = 0
        while i < len(pairs):
            j=i
            while j > 0:
                if(pairs[j].key < pairs[j-1].key):
                    temp = pairs[j-1]
                    pairs[j-1]=pairs[j]
                    pairs[j]=temp
                j = j-1
            i=i+1
            ret.append(pairs[:])
        return ret

        