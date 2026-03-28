# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
N = int(input())

a = b = 1
for _ in range(2, N + 1):
    a, b = b, (a + b) % 15746
print(b)
