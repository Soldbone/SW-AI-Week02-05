# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
"""
요세푸스 문제와 연관 있다고 한다.
공식이 있다.
"""

from collections import deque

N = int(input())
deck = deque(range(1, N + 1))

while N > 1:
    deck.popleft()
    deck.append(deck.popleft())
    N -= 1

print(deck[0])
