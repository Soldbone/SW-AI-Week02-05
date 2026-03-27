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

    a, b = 0, 1  # 각각 F(0), F(1)

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# print(fib_tabulation(50))
print(fib_rolling(50))
