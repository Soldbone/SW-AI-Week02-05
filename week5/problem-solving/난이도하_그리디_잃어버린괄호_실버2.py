# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

"""마이너스(-) 기호가 있는 부분에 덧셈이 있다면 최대한 많이 해야 한다. 그리고 나머지는 그냥 더하면 된다."""
# 엣지 케이스:
# "-"가 없는 경우
# "-"가 1개만 존재하는 경우

# expression = input()
# split_minus = expression.split("-")

# # "-"가 없는 경우
# if len(split_minus) == 1:
#     candidate = split_minus[0].split("+")
#     total = 0
#     start = 0
#     for i in range(start, len(candidate)):
#         num = candidate[i]
#         total += int(num)
#     print(total)
# # "-"가 있는 경우
# else:
#     total = 0
#     start = 1

#     if "+" not in split_minus[0]:
#         total = int(split_minus[0])
#     else:
#         plus_terms = split_minus[0].split("+")
#         for plus in plus_terms:
#             total += int(plus)

#     for i in range(start, len(split_minus)):
#         term = split_minus[i]
#         add_in_minus = 0
#         if "+" in term:
#             add_term = term.split("+")
#             for add in add_term:
#                 add_in_minus += int(add)
#         else:
#             add_in_minus += int(term)
#         total -= add_in_minus

#     print(total)

"""
san00님 풀이 참고
리팩토링 - '-'(마이너스)가 있는 경우와 없는 경우를 꼭 나눠야 할까?
그냥 나눠진 거 기준으로 처음엔 더하고 이후부터는 빼주면 된다.
그리고 split("+")을 할 때 굳이 있는지 확인 안 해도 된다. 그냥 그대로 리스트로 나오기 때문이다.
"""
expression = input()
split_minus = expression.split("-")

total_sum = sum(map(int, split_minus[0].split("+")))

for part in split_minus[1:]:
    total_sum -= sum(map(int, part.split("+")))

print(total_sum)
