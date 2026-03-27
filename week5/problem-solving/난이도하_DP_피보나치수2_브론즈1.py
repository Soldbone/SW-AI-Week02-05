# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

def fibo(n, memo=None):
    if memo is None:
        memo = dict()
    
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]


n = int(input())
print(fibo(n))