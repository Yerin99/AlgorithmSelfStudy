students_hw = [False]*30

for i in range(28):
    student_number = int(input())
    students_hw[student_number - 1] = True

for j in range(30):
    if not students_hw[j]:
        print(j+1)
