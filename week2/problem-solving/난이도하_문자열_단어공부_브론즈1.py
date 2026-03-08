# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

word = input()
count_for_char = {}
for char in word:
    ignore_case_char = char.upper()
    if ignore_case_char not in count_for_char:
        count_for_char[ignore_case_char] = 1
    else:
        count_for_char[ignore_case_char] += 1

# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력
# 무식하게 풀어보자:
# 순회해서 가장 큰 값을 찾는다.
# 순회해서 가장 큰 값을 갖는 키의 개수를 확인한다.
max_count = count_for_char[word[0].upper()]
for char, count in count_for_char.items():
    if count > max_count:
        max_count = count

most_freq_chars = []
for char, count in count_for_char.items():
    if count == max_count:
        most_freq_chars.append(char)

if len(most_freq_chars) == 1:
    print(most_freq_chars[0])
else:
    print("?")
