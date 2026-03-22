# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 게임판 크기
N = int(input())

# 맵 로딩
game_map = []
for _ in range(N):
    game_map.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
# 아래쪽 오른쪽
IS_POSSIBLE = False


def dfs(game_map, coord: tuple, visited):
    global IS_POSSIBLE
    x, y = coord
    visited[x][y] = True

    # 범위 밖

    if game_map[x][y] == -1:
        IS_POSSIBLE = True
        return

    if game_map[x][y] == 0:
        # 더 이상 진행하지 않아도 됨 (그러나 어떻게?)
        return

    for i in range(2):
        movable = game_map[x][y]
        if x + game_map[x][y] < N:
            if not visited[x + movable][y]:
                coord = (x + movable, y)
                dfs(game_map, coord, visited)

        if y + game_map[x][y] < N:
            if not visited[x][y + movable]:
                coord = (x, y + movable)
                dfs(game_map, coord, visited)


dfs(game_map, (0, 0), visited)
if IS_POSSIBLE:
    print("HaruHaru")
else:
    print("Hing")
