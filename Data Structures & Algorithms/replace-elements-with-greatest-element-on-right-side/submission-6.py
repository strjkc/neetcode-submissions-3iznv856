class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    # 2,4,5,3,1,2
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            curr = arr[i]
            arr[i] = curr_max
            curr_max = max(curr, curr_max)
        return arr

