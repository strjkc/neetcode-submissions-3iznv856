class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    # 2,4,5,3,1,2
        for i in range(len(arr)-1):
            curr_max = 0
            k = i + 1
            for j in range(k, len(arr)):
                if arr[j] > curr_max:
                    curr_max = arr[j]
            arr[i] = curr_max
        arr[-1] = -1
        return arr

