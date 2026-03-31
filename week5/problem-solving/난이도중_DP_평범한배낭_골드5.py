# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(len(items)):
    for w in range(K, 0, -1):
        if w >= items[i][0]:
            dp[w] = max(dp[w], dp[w - items[i][0]] + items[i][1])
print(dp[K])
