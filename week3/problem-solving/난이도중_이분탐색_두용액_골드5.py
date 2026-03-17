# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline
N = int(input())

liquid = sorted(list(map(int, input().split())))

i = 0
j = len(liquid) - 1 - i
min = float("inf")
min_index = (None, None)
while i < j:
    mixture = liquid[i] + liquid[j]
    if abs(mixture) < abs(min):
        min = mixture
        min_index = (i, j)

    if mixture >= 0:
        j -= 1
    else:
        i += 1

print(liquid[min_index[0]], liquid[min_index[1]])
