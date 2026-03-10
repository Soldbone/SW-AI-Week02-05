# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

N = int(input())
nums = list(map(int, input().split()))

# 모든 경우의 수를 만든다.  -> HOW?
# 모든 경우의 수마다 식의 값을 계산하여 최대값을 찾는다.

# visited = [False] * N

# max = -1


# def perm(path: list):
#     global max
#     if len(path) == N:
#         acc = 0
#         for i in range(len(path) - 1):
#             acc += abs(path[i] - path[i + 1])

#         if acc > max:
#             max = acc
#         return

#     for i in range(len(nums)):
#         if not visited[i]:
#             path.append(nums[i])
#             visited[i] = True
#             perm(path)
#             path.pop()
#             visited[i] = False


# perm([])
# print(max)



## permutations 라이브러리 사용
from itertools import permutations

answer = -1

for perm in permutations(nums):
    total = 0
    for i in range(N - 1):
        total += abs(perm[i] - perm[i + 1])
    answer = max(answer, total)

print(answer)
