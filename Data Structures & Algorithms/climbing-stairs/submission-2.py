class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def sub(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            if i not in memo:
                res = sub(i + 1) + sub(i + 2)
                memo[i] = res
            return memo[i]
        return sub(0)