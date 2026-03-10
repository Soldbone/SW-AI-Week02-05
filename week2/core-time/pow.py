# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 음수 지수 처리
        if n < 0:
            x = 1 / x
            n = -n

        def power(x, n):
            if n == 0:
                return 1
            
            half = power(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        return power(x, n)
