# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# word = input().upper()
# count_for_char = {}
# max_count = 1
# # 등록 시 최대값을 기억하도록 약간 개선
# for char in word:
#     ignore_case_char = char
#     if ignore_case_char not in count_for_char:
#         count_for_char[ignore_case_char] = 1
#     else:
#         count_for_char[ignore_case_char] += 1
#         count = count_for_char[ignore_case_char]
#         if count > max_count:
#             max_count = count

# # 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력
# # 순회해서 가장 큰 값을 갖는 키를 리스트에 저장하고 리스트의 길이를 확인한다.
# most_freq_chars = []
# for char, count in count_for_char.items():
#     if count == max_count:
#         most_freq_chars.append(char)

# if len(most_freq_chars) == 1:
#     print(most_freq_chars[0])
# else:
#     print("?")

"""
ChatGPT의 도움을 받아 개선한 버전
"""
word = input().upper()

counts_for_alpha = [0] * 26

for char in word:
    counts_for_alpha[ord(char) - ord("A")] += 1

max_count = max(counts_for_alpha)

if counts_for_alpha.count(max_count) == 1:
    print(chr(counts_for_alpha.index(max_count) + ord("A")))
else:
    print("?")
