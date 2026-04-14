class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = {}
        for num in nums:
            n = uniques.get(num, None)
            if n is None:
                uniques[num] = True
            else:
                return True
        return False