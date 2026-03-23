# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(N - 1):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

parents = [-1 for _ in range(N + 1)]

queue = deque([1])
visited[1] = True
while queue:
    i = queue.popleft()
    for neighbor in graph[i]:
        # 차례대로 보게 되는데, 1의 neighbor는 무조건 자식이다. 자식들의 parents[] 정보에 1을 적어준다.
        # 1의 neighbor와 연결된 노드는 무조건 자식이다.
        if not visited[neighbor]:
            parents[neighbor] = i
            visited[neighbor] = True
            queue.append(neighbor)

for i in range(2, N + 1):
    print(parents[i])
