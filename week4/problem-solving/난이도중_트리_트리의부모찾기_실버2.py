# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

parents = [-1] * (N + 1)
queue = deque([1])
parents[1] = 1
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        # 1의 neighbor는 무조건 자식이다. 자식들의 parents[] 정보에 1을 적어준다.
        # 1의 neighbor와 연결된 노드는 무조건 자식이다.
        if parents[neighbor] == -1:
            parents[neighbor] = current
            queue.append(neighbor)

for i in range(2, N + 1):
    print(parents[i])
