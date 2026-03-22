# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

import sys

# 중심 노드를 정한다. (0으로 정하자.)
n, m = map(int, input().split())

edges = []

# 중심 노드에 리프 노드를 M개 붙인다.
for i in range(1, m + 1):
    edges.append((0, i))

# 지금까지 사용된 노드는 M+1개이다.
# 나머지 노드는 N - (M+1)개이다.
# 나머지 노드는 임의의 리프 노드 뒤에 연속적으로 붙인다.
prev = 1
for i in range(m + 1, n):
    edges.append((prev, i))
    prev = i

for edge in edges:
    sys.stdout.write(f"{edge[0]} {edge[1]}\n")
