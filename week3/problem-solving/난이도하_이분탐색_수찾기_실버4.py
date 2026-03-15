# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

N = int(input())
A = dict.fromkeys(input().split(), 0)
M = int(input())
nums = input().split()

for word in nums:
    print(int(word in A))
