# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    data = input().rstrip()
    row = []
    for col in data:
        row.append(int(col))
    board.append(row)


def bfs(start: tuple, board):
    from collections import deque

    visited = [[False] * M for _ in range(N)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    while queue:
        x, y = queue.popleft()

        if (x == N - 1) and (y == M - 1):
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N) and (not visited[nx][ny]) and (board[nx][ny] != 0):
                count += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return count

print(bfs((0,0), board))
