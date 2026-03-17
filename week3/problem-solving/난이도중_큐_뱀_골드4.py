# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

import sys
from collections import deque

"""
1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
"""

input = sys.stdin.readline
N = int(input())

K = int(input())
apple_coord = []
for _ in range(K):
    apple_coord.append(tuple(map(int, input().split())))
apple_coord = dict.fromkeys(apple_coord, 1)

# 방향 설정 [오른쪽, 아래, 왼쪽, 위쪽]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_direction = 0

face_direction = directions[cur_direction]
head = (1, 1)
tail = deque()
timer = 0
GAME_OVER = False
L = int(input())
for _ in range(L):
    command = input().split()
    sec = int(command[0])
    new_direct = command[1]

    interval = sec - timer
    while interval > 0:
        timer += 1
        x = head[0] + face_direction[0]
        y = head[1] + face_direction[1]

        head = (x, y)

        # 벽과 부딪히면 게임 오버
        if (head[0] > N) or (head[1] > N) or (head[0] < 1) or (head[1] < 1):
            GAME_OVER = True
            break

        # 몸과 부딪히면 게임 오버
        if head in tail:
            GAME_OVER = True
            break

        # 사과가 없으면 tail 줄이기
        if (apple_coord.get(head) is None) or (apple_coord.get(head) == 0):
            if tail:
                tail.popleft()

        # 사과가 있다면 꼬리는 움직이지 않음
        if apple_coord.get(head) == 1:
            if head == (1, 2) or head == (2, 1):
                tail.append((1, 1))
            apple_coord[head] = 0

        tail.append(head)
        interval -= 1

    if GAME_OVER:
        break

    if new_direct == "D":
        cur_direction = (cur_direction + 1) % len(directions)
    if new_direct == "L":
        cur_direction = (cur_direction - 1) % len(directions)

    face_direction = directions[cur_direction]

if not GAME_OVER:
    GAME_OVER = False
    while not GAME_OVER:
        timer += 1

        x = head[0] + face_direction[0]
        y = head[1] + face_direction[1]

        head = (x, y)

        # 벽과 부딪히면 게임 오버
        if (head[0] > N) or (head[1] > N) or (head[0] < 1) or (head[1] < 1):
            GAME_OVER = True
            break

        # 몸과 부딪히면 게임 오버
        if head in tail:
            GAME_OVER = True
            break

        # 사과가 없으면 tail 줄이기
        if (apple_coord.get(head) is None) or (apple_coord.get(head) == 0):
            if tail:
                tail.popleft()

        # 사과가 있다면 꼬리는 움직이지 않음
        if apple_coord.get(head) == 1:
            apple_coord[head] = 0

        tail.append(head)

print(timer)
