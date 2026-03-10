# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
N = int(input())

# 하노이 옮기는 개수 점화식.
# n번째 블록 위의 T(n-1)개를 옮기고  n번째 블록을 제일 오른쪽으로 옮기고 n
count = 2**N - 1
print(count)

def hanoi(src, dest, via, n):
    if n > 20:
        return

    if n == 1:
        print(src, dest)
        return
    else:
        hanoi(src, via, dest, n-1)
        print(src, dest)
        hanoi(via, dest, src, n-1)

hanoi("1", "3", "2", N)
