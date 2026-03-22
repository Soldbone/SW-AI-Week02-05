# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

import sys

input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        run_test_case()


def run_test_case():
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    find_least_airplane_path(N, graph)


def find_least_airplane_path(N, graph: list[list[int]]):
    to_visit = [True] * (N + 1)
    count = 0

    def _dfs(node):
        to_visit[node] = False
        nonlocal count

        for neighbor in graph[node]:
            if to_visit[neighbor]:
                count += 1
                _dfs(neighbor)

    _dfs(1)
    print(count)


main()
