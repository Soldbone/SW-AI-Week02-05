# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
import sys

input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    color = [-1] * (V + 1)  # 0 or 1
    for _ in range(E):
        src, dest = map(int, input().split())
        graph[src].append(dest)
        graph[dest].append(src)
    bfs()

def bfs(start, graph, color):
    from collections import deque
    queue = deque([start])
    color[start] = 0
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if color[node] == 0:
                    color[neighbor] = 1
                else:
                    color[neighbor] = 0
    