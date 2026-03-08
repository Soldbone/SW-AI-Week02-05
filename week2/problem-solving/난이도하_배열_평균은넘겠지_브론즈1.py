# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
C = int(input())


def get_ratio_of_above_average_students(students: list) -> float:
    # 평균을 구한다
    num_of_students = students[0]
    average = (sum(students) - num_of_students) / num_of_students

    # 평균을 넘는 학생의 숫자를 구한다
    num_of_above_average_students = 0
    for i in range(1, num_of_students + 1):
        if students[i] > average:
            num_of_above_average_students += 1

    # 전체 학생 수에서 평균을 넘는 학생의 비율을 백분율로 계산한다
    ratio = num_of_above_average_students / num_of_students * 100

    return ratio


for _ in range(C):
    student_scores = list(map(int, input().split()))
    print(f"{get_ratio_of_above_average_students(student_scores):.3f}%")
