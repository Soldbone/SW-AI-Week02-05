# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

visited = [False] * (N + 1)


def dfs(start, visited, graph):
    count = 0

    def _dfs(start, visited, graph):
        nonlocal count
        visited[start] = True

        for neighbor in graph[start]:
            if not visited[neighbor]:
                count += 1
                _dfs(neighbor, visited, graph)

    _dfs(start, visited, graph)
    return count


print(dfs(1, visited, graph))
