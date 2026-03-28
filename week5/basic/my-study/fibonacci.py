"""
###################
    피보나치 수열
###################
"""


def fib_tabulation(n):
    if n <= 1:
        return n

    tab = [0] * (n + 1)
    tab[1] = 1

    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]

    return tab[n]


def fib_rolling(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# print(fib_tabulation(50))
# print(fib_rolling(50))


"""
###################
    계단 오르기
###################
"""


def climb_stairs(n):
    """
    계단 오르기 (상향식 DP)

    Args:
        n: 계단의 수

    Returns:
        n번째 계단까지 오르는 방법의 수
    """
    # TODO: dp 배열 생성 및 초기화
    dp = [0] * (n + 2)
    dp[0] = dp[1] = 1

    # TODO: 작은 문제부터 차례로 계산
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


for i in range(1, 11):
    result = climb_stairs(i)
    print(f"{i}번 계단: {result}가지")
