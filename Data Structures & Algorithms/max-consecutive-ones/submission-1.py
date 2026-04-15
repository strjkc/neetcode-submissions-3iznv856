class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0
        counter = 0
        for n in nums:
            if n == 1:
                counter += 1
            else:
                curr_max = max(counter, curr_max)
                counter = 0
        curr_max = max(counter, curr_max)
        return curr_max
        