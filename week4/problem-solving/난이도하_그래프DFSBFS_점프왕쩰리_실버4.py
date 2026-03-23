# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

### BFS - 벡터 개념 사용해보기
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
queue = deque([(0, 0)])
visited[0][0] = True

# r(ow), c(olumn)
while queue:
    r, c = queue.popleft()

    if board[r][c] == -1:
        print("HaruHaru")
        break

    jump = board[r][c]

    # 오른쪽, 아래
    moves = [(0, jump), (jump, 0)]

    for move in moves:
        dr, dc = move
        nr, nc = r + dr, c + dc
        if nr < n and nc < n and not visited[nr][nc]:
            visited[nr][nc] = True
            queue.append((nr, nc))
else:
    print("Hing")


# ### BFS - ChatGPT 사용
# from collections import deque
# import sys

# input = sys.stdin.readline

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]

# visited = [[False] * n for _ in range(n)]
# queue = deque([(0, 0)])
# visited[0][0] = True

# # r(ow), c(olumn)
# while queue:
#     r, c = queue.popleft()

#     if board[r][c] == -1:
#         print("HaruHaru")
#         break

#     jump = board[r][c]

#     nr, nc = r + jump, c
#     if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
#         visited[nr][nc] = True
#         queue.append((nr, nc))

#     nr, nc = r, c + jump
#     if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
#         visited[nr][nc] = True
#         queue.append((nr, nc))
# else:
#     print("Hing")


# ### DFS - ChatGPT가 개선해 준 버전
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# visited = [[False] * N for _ in range(N)]


# def dfs(x, y):
#     if x >= N or y >= N:
#         return False

#     if visited[x][y]:
#         return False

#     if board[x][y] == -1:
#         return True

#     visited[x][y] = True
#     jump = board[x][y]

#     if jump == 0:
#         return False

#     return dfs(x + jump, y) or dfs(x, y + jump)


# print("HaruHaru" if dfs(0, 0) else "Hing")


### DFS - 내가 작성한 버전
# # 게임판 크기
# N = int(input())

# # 맵 로딩
# game_map = []
# for _ in range(N):
#     game_map.append(list(map(int, input().split())))

# visited = [[False] * N for _ in range(N)]
# # 아래쪽 오른쪽
# IS_POSSIBLE = False


# def dfs(game_map, coord: tuple, visited):
#     global IS_POSSIBLE
#     x, y = coord
#     visited[x][y] = True

#     # 범위 밖

#     if game_map[x][y] == -1:
#         IS_POSSIBLE = True
#         return

#     if game_map[x][y] == 0:
#         # 더 이상 진행하지 않아도 됨 (그러나 어떻게?)
#         return

#     for i in range(2):
#         movable = game_map[x][y]
#         if x + game_map[x][y] < N:
#             if not visited[x + movable][y]:
#                 coord = (x + movable, y)
#                 dfs(game_map, coord, visited)

#         if y + game_map[x][y] < N:
#             if not visited[x][y + movable]:
#                 coord = (x, y + movable)
#                 dfs(game_map, coord, visited)


# dfs(game_map, (0, 0), visited)
# if IS_POSSIBLE:
#     print("HaruHaru")
# else:
#     print("Hing")
