# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# preorder = []
# while True:
#     try:
#         line = input().strip()
#         if not line:
#             break
#         preorder.append(int(line))
#     except:
#         break


# def post_order(start, end):
#     if start > end:
#         return

#     root = preorder[start]

#     split = end + 1
#     for i in range(start + 1, end + 1):
#         if preorder[i] > root:
#             split = i
#             break

#     # 왼쪽 서브트리
#     post_order(start + 1, split - 1)
#     # 오른쪽 서브트리
#     post_order(split, end)
#     print(root)


# post_order(0, len(preorder) - 1)


import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        preorder.append(int(line))
    except:
        break

idx = 0
n = len(preorder)
result = []


def build(lower, upper):
    global idx

    if idx >= n:
        return

    value = preorder[idx]

    if not (lower < value < upper):
        return

    idx += 1
    build(lower, value)  # 왼쪽
    build(value, upper)  # 오른쪽
    result.append(value)  # 후위 순회


build(float("-inf"), float("inf"))
print("\n".join(map(str, result)))
