# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

"""
1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

# 사과 위치 저장
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())

turns = {}
for _ in range(L):
    x, c = input().split()
    turns[int(x)] = c

# 오른쪽, 아래, 왼쪽, 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

direction = 0
time = 0

# 뱀의 몸: (행, 열)
snake = deque()
snake.append((0, 0))
board[0][0] = 2

while True:
    time += 1

    head_r, head_c = snake[-1]
    nr = head_r + dr[direction]
    nc = head_c + dc[direction]

    # 벽 충돌
    if not (0 <= nr < N and 0 <= nc < N):
        break

    # 자기 몸 충돌
    if board[nr][nc] == 2:
        break

    # 머리 이동
    if board[nr][nc] == 1:
        # 사과가 있으면 꼬리 유지
        board[nr][nc] = 2
        snake.append((nr, nc))
    else:
        # 사과가 없으면 꼬리 제거
        tail_r, tail_c = snake.popleft()
        board[tail_r][tail_c] = 0

        board[nr][nc] = 2
        snake.append((nr, nc))

    # 방향 전환
    if time in turns:
        if turns[time] == "D":
            direction = (direction + 1) % 4
        else:  # 'L'
            direction = (direction - 1) % 4

print(time)


# import sys
# from collections import deque


# input = sys.stdin.readline
# N = int(input())

# K = int(input())
# apple_coord = []
# for _ in range(K):
#     apple_coord.append(tuple(map(int, input().split())))
# apple_coord = dict.fromkeys(apple_coord, 1)

# # 방향 설정 [오른쪽, 아래, 왼쪽, 위쪽]
# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# cur_direction = 0

# face_direction = directions[cur_direction]
# head = (1, 1)
# tail = deque()
# timer = 0
# GAME_OVER = False
# L = int(input())
# for _ in range(L):
#     command = input().split()
#     sec = int(command[0])
#     new_direct = command[1]

#     interval = sec - timer
#     while interval > 0:
#         timer += 1
#         x = head[0] + face_direction[0]
#         y = head[1] + face_direction[1]

#         head = (x, y)

#         # 벽과 부딪히면 게임 오버
#         if (head[0] > N) or (head[1] > N) or (head[0] < 1) or (head[1] < 1):
#             GAME_OVER = True
#             break

#         # 몸과 부딪히면 게임 오버
#         if head in tail:
#             GAME_OVER = True
#             break

#         # 사과가 없으면 tail 줄이기
#         if (apple_coord.get(head) is None) or (apple_coord.get(head) == 0):
#             if tail:
#                 tail.popleft()

#         # 사과가 있다면 꼬리는 움직이지 않음
#         if apple_coord.get(head) == 1:
#             if head == (1, 2) or head == (2, 1):
#                 tail.append((1, 1))
#             apple_coord[head] = 0

#         tail.append(head)
#         interval -= 1

#     if GAME_OVER:
#         break

#     if new_direct == "D":
#         cur_direction = (cur_direction + 1) % len(directions)
#     if new_direct == "L":
#         cur_direction = (cur_direction - 1) % len(directions)

#     face_direction = directions[cur_direction]

# if not GAME_OVER:
#     GAME_OVER = False
#     while not GAME_OVER:
#         timer += 1

#         x = head[0] + face_direction[0]
#         y = head[1] + face_direction[1]

#         head = (x, y)

#         # 벽과 부딪히면 게임 오버
#         if (head[0] > N) or (head[1] > N) or (head[0] < 1) or (head[1] < 1):
#             GAME_OVER = True
#             break

#         # 몸과 부딪히면 게임 오버
#         if head in tail:
#             GAME_OVER = True
#             break

#         # 사과가 없으면 tail 줄이기
#         if (apple_coord.get(head) is None) or (apple_coord.get(head) == 0):
#             if tail:
#                 tail.popleft()

#         # 사과가 있다면 꼬리는 움직이지 않음
#         if apple_coord.get(head) == 1:
#             apple_coord[head] = 0

#         tail.append(head)

# print(timer)
