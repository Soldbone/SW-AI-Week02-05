# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

# 동전 리스트를 정렬한다.
# queue에 각 동전을 1개씩 넣어 준다.
# 이후에는 각 동전의 기준 가치(첫번째 요소)보다 크거나 같은 요소들만 뒤에 각각 추가해서 queue에 넣어준다.
# 원하는 값이 되었는지 확인하고 min_count를 업데이트 한다.
n, k = map(int, input().split())

coins = set()
for _ in range(n):
    coin = int(input())
    coins.add(coin)
coins = sorted(coins)

def bfs(n: int, k: int):
    from collections import deque

    queue = deque([i for i in range(len(coins))])
    while queue:
        coins_in_hand = []
        pass
