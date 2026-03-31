# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        return dp[n]

class Solution2:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]
