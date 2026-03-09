# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

"""
!! 문제를 잘 읽자 !!
# 포인트: join(), 빈 left_groups/right_groups은 0개로 처리, zfill(), list concatenation
"""
# 1. ::를 기준으로 왼쪽과 오른쪽으로 나눈다.
# 2. 왼쪽과 오른쪽의 요소를 :으로 나누어 그룹을 구한다.
# 3. 그룹의 개수를 통해서 ::에 채울 0000 그룹 수를 구한다.
# 4. 왼쪽, 0000 그룹, 오른쪽을 합쳐 결과를 출력한다.

compressed_ipv6 = input()

if "::" in compressed_ipv6:
    left, right = compressed_ipv6.split("::")

    # "ab:cd:" -> [ab, cd, '']
    # "" -> []이어야 되는데 [""] 이게 나오므로 따로 처리
    left_groups = left.split(":") if left else []
    right_groups = right.split(":") if right else []

    missing = 8 - (len(left_groups) + len(right_groups))
    groups = left_groups + missing * ["0000"] + right_groups

else:
    groups = compressed_ipv6.split(":")

print(":".join(group.zfill(4) for group in groups))
