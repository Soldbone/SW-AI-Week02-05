# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
T = int(input())

for _ in range(T):
    # 반복 횟수와 문자열 입력 받기
    R, word = input().split()
    R = int(R)

    # 결과 문자열 초기화
    result_word = ""

    # 문자열의 각 문자를 반복 횟수만큼 반복 생성해서 결과 문자열에 더하기
    for char in word:
        result_word += char * R

    # 결과 문자열 출력
    print(result_word)
