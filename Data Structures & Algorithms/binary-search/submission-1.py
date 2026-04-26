class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + (high-low)) //2
            n = nums[mid]
            if n == target:
                return mid
            elif n > target:
                high = mid - 1
            elif n < target:
                low = mid + 1
        return -1
