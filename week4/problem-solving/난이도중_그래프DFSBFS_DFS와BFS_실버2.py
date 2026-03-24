# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
import sys

input = sys.stdin.readline
N, M, V = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

for edge in graph:
    edge.sort()


def dfs_stack(start, graph):
    visited = [False] * len(graph)
    stack = [start]
    result = []
    while stack:
        node = stack.pop()

        if not visited[node]:
            result.append(node)
            visited[node] = True
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    return result


print(dfs_stack(V, graph))


def bfs(start, graph):
    from collections import deque

    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result


print(bfs(V, graph))


# def dfs_recursion(start, graph, visited):
#     result = []

#     def _dfs(start, graph, visited):
#         nonlocal result
#         visited[start] = True
#         result.append(start)

#         for neighbor in graph[start]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 _dfs(neighbor, graph, visited)

#     _dfs(start, graph, visited)
#     return result


# print(dfs_recursion(V, graph, visited))
