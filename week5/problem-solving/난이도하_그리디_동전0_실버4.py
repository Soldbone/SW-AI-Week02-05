# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

total_count = 0
coins = reversed(coins)
for coin in coins:
    count, K = divmod(K, coin)
    total_count += count
    if K == 0:
        break
print(total_count)
