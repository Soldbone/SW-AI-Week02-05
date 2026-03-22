# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

import sys

input = sys.stdin.readline


def dfs(graph, start, visited):
    stack = [start]
    count = 0
    visited[start] = True

    while stack:
        current = stack.pop()

        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                count += 1

    return count


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    print(dfs(graph, 1, visited))
