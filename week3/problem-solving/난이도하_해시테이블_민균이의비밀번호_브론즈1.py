# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

import sys
input = sys.stdin.readline

N = int(input())
rainbow = set()

for _ in range(N):
    word = input().strip()
    if (word[::-1] in rainbow) or (word == word[::-1]):
        break
    else:
        rainbow.add(word)

word_length = len(word)
print(word_length, word[word_length // 2])
