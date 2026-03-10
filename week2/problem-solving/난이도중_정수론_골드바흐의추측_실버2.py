# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

# 전적으로 AI 도움 받음. 흐름을 혼자 못 쫓아 가겠음

# 더해서 n을 만드는 두 소수(골드바흐 파티션) 구하기
# 골드바흐 파티션이 여러 개라면 두 소수의 차이가 가장 작은 것을 출력
T = int(input())

nums = [int(input()) for _ in range(T)]
max_n = max(nums)

# 문제에서 주어진 n의 최댓값인 10000개를 만들어도 됨. 그러면 위의 nums와 amx()도 필요 없음
is_prime = [True] * max_n
is_prime[0] = is_prime[1] = 0

for i in range(2, int(max_n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_n, i):
            is_prime[j] = False

# a + b = n
# b = n - a
# |a - b| = |2a - n|의 최솟값은 0, 그때의 a값은 n/2
for n in nums:
    a = n // 2
    while a >= 2:
        b = n - a
        if is_prime[a] and is_prime[b]:
            print(a, b)
            break
        a -= 1
