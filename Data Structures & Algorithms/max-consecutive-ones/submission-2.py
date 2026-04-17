class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_max = 0
        for n in nums:
            if n == 1:
                cur_max += 1
            else:
                if cur_max > max_count:
                    max_count = cur_max
                cur_max = 0
        max_count = max(cur_max, max_count)           
        return max_count
        