class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        prefix = 1
        for i, num in enumerate(nums):
            out.append(prefix)
            prefix = prefix * num
        print(out)

        sufix = 1
        for i in range(len(nums) -1 , -1, -1):
            print(nums[i])
            print(sufix)
            out[i] *= sufix
            sufix *= nums[i]
            print(sufix)
        print(out)
        return out