# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

# 0. 종이가 한 칸이면 count하고 return
# 1. 색 확인 (이중 for문)
# 2. 색이 하나라도 다르면 분할
# 3. 색이 모두 같으면 count하고 return

# 오른쪽 반열림 구간임에 유의 (range 방식 반영)
# 0은 row_start로 변경 필요, N은 row_end로 변경 필요
# 왼쪽 위:      [0 ~ N//2+1][0 ~ N//2+1]
# 오른쪽 위:    [0 ~ N//2+1][N//2+1 ~ N]
# 왼쪽 아래:    [N//2+1 ~ N][0 ~ N//2+1]
# 오른쪽 아래:  [N//2+1 ~ N][N//2+1 ~ N]

import sys

input = sys.stdin.readline
N = int(input())

entire_paper = [list(map(int, input().split())) for _ in range(N)]


blue_count = 0
white_count = 0


def make_paper(row_start, col_start, n):
    # end 구간은 반열림 구간으로 둬서 숫자가 1큼에 유의
    global blue_count
    global white_count

    row_end = row_start + n
    col_end = col_start + n
    color = entire_paper[row_start][col_start]
    if row_end - row_start == 1:
        if color == 0:
            white_count += 1
        else:
            blue_count += 1
        return

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if color != entire_paper[row][col]:
                # 왼쪽 위:      [0 ~ N//2][0 ~ N//2]
                make_paper(row_start, col_start, n // 2)
                # 오른쪽 위:    [0 ~ N//2][N//2 ~ N]
                make_paper(row_start, col_start + n // 2, n // 2)
                # 왼쪽 아래:    [N//2 ~ N][0 ~ N//2]
                make_paper(row_start + n // 2, col_start, n // 2)
                # 오른쪽 아래:  [N//2 ~ N][N//2 ~ N]
                make_paper(row_start + n // 2, col_start + n // 2, n // 2)
                return

    # 색이 모두 같으면 count하고 return
    if color == 0:
        white_count += 1
    else:
        blue_count += 1
    return


make_paper(0, 0, N)
print(white_count, blue_count, sep="\n")
