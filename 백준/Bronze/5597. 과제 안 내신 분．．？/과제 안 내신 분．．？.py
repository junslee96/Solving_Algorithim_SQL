# 28명의 제출자의 출석번호를 입력받습니다.
submissions = []
for _ in range(28):
    n = int(input())
    submissions.append(n)

# 1부터 30까지의 전체 학생 출석번호 집합을 생성합니다.
all_students = set(range(1, 31))

# 제출한 학생들의 출석번호 집합을 구합니다.
submitted_students = set(submissions)

# 제출하지 않은 학생의 출석번호를 구한 후 정렬합니다.
not_submitted_students = sorted(all_students - submitted_students)

# 제출하지 않은 학생 중 가장 작은 번호와 그 다음 번호를 출력합니다.
print(not_submitted_students[0])
print(not_submitted_students[1])
