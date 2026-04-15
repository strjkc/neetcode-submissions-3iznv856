class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    # 2,4,5,3,1,2
        for i in range(len(arr)-1):
            curr_max = max(arr[i+1:])
            arr[i] = curr_max
        arr[-1] = -1
        return arr

