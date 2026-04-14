class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {} #number as key and index as value
        for i, n in enumerate(nums):
            ref[n] = i
        for i, n in enumerate(nums):
            res = target - n
            index = ref.get(res, None)
            if index and index != i:
                return [i, index]


