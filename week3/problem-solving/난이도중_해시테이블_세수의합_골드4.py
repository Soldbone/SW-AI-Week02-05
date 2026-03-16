# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# 두 수의 합을 저장해놓고 뒤에서부터 저장된 두 수의 합을 뺀 값이 후보에 있는지 확인해보면 어떨까

import sys

input = sys.stdin.readline
candidate = set()
nums = []
N = int(input())
for _ in range(N):
    nums.append(int(input()))

nums.sort()
for i in range(N):
    for j in range(i, N):
        candidate.add(nums[i] + nums[j])

BREAK_NESTED_FOR = False
for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if nums[i] - nums[j] in candidate:
            print(nums[i])
            BREAK_NESTED_FOR = True
            break
    if BREAK_NESTED_FOR:
        break
