# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for weight, value in items:
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)
print(dp[K])
