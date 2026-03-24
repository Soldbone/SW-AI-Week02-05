# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
from collections import deque
import sys
"""
의존성 개수가 같은 작업 중 가장 오래 걸리는 작업에 걸리는 시간을 더해주면 된다 (아마도)
"""
input = sys.stdin.readline

N = int(input())
demand_time = [None]
graph = [[] for _ in range(N)]
data = list(map(int, input().split()))
for _ in range(N):
    data = list(map(int, input().split()))
    if len(data) != 2:
        for i in range(data[])



def topological_sort(vertices, edges, graph):
    in_degree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # 진입 차수가 0인 정점들을 큐에 추가
    queue = deque([i for i in range(vertices) if in_degree[i] == 0])

    time = 0
    ## 정점을 꺼내 인접한 정점들의 진입 차수 감소
    while queue:
        q_size = len(queue)
        max_time = -1
        for _ in range(q_size):
            node = queue.popleft()
            if time[node] > max_time:
                max_time = time[node]

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        time += max_time

    if len(result) != vertices:
        return -1

    return time
