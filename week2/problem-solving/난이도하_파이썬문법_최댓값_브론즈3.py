# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

N = 9
max_num = int(input())
max_location = 1
for i in range(1, N):
    num = int(input())
    if num > max_num:
        max_location = i + 1
        max_num = num

print(max_num)
print(max_location)
