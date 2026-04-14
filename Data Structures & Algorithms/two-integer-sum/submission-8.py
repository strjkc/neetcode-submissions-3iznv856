class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(0, len(nums) - 1):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i, j] 

        i = 0
        j = 1
        while i < len(nums) - 1:
            if nums[i] + nums[j] == target:
                return [i,j]
            elif j == len(nums) -1:
                i += 1
                j = i + 1
            else: 
                j += 1