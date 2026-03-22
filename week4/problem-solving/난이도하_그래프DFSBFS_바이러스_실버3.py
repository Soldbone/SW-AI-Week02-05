# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

import sys

input = sys.stdin.readline

num_com = int(input())
num_com_in_net = int(input())

graph = [[] for _ in range(num_com + 1)]
visited = [False] * (num_com + 1)
for _ in range(num_com_in_net):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

count = 0
def dfs(graph, node, visited):
    global count
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += 1
            dfs(graph, neighbor, visited)

dfs(graph, 1, visited)
print(count)