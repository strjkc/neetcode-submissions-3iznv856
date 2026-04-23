class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, number in enumerate(nums):
            diff = target - number 
            if diff in m:
                return [m[diff], i]
            m[number] = i
        return -1


