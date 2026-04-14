class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        numbers = set(nums)
        max_seq_len = 0

        for num in nums:
            if num -1 not in numbers:
                leng = 1
                while (num + leng) in numbers:
                    leng += 1
                max_seq_len = max(leng, max_seq_len)
        return max_seq_len