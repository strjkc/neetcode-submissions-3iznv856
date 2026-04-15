class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res_arr = [0] * (len(nums) * 2)
        for i, num in enumerate(nums):
            res_arr[i] = num

        for i, num in enumerate(nums):
            res_arr[i + len(nums)] = num
        
        return res_arr
 