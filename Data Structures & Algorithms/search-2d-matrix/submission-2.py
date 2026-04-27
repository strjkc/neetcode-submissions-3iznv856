class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        o_low = 0
        o_high = len(matrix) -1
        while o_low <= o_high:
            o_mid = (o_low + o_high) // 2
            arr = matrix[o_mid]
            if target < arr[0]:
                o_high = o_mid - 1 
                continue
            if target > arr[len(arr)-1]:
                o_low = o_mid + 1
                continue
            i_low = 0
            i_high = len(arr) -1
            while i_low <= i_high:
                i_mid = (i_low + i_high) // 2
                if arr[i_mid] == target:
                    return True
                elif arr[i_mid] < target:
                    i_low = i_mid + 1
                elif arr[i_mid] > target:
                    i_high = i_mid - 1
            return False
        return False
        