# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 2)
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    def climbStairs2(self, n: int) -> int:
        a, b = 1, 2
        if n == 1:
            return 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b
