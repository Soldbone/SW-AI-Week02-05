# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629


a, b, c = map(int, input().split())


def pow_modulo(num, n):
    if n == 1:
        return num % c

    half_exp = pow_modulo(num, n // 2)
    if n % 2 == 0:
        return (half_exp * half_exp) % c
    else:
        return (num * half_exp * half_exp) % c


print(pow_modulo(a, b))



## 반복문 버전
a, b, c = map(int, input().split())

result = 1
num = a % c
n = b

while n > 0:
    if n % 2 == 1:
        result = (result * num) % c
    num = (num * num) % c
    n //= 2

print(result)
