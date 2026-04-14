class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = []
        for num in nums:
            if num not in uniques:
                uniques.append(num)
            else:
                return True
        return False