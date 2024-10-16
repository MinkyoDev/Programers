def solution(n, losts, reserves):
    students = []
    for i in range(1, n+1):
        have = 1
        if i in reserves:
            have += 1
        if i in losts:
            have -= 1
        students.append(have)

    for i in range(len(students)):
        if students[i] == 0:
            if i - 1 >= 0 and students[i-1] == 2:
                students[i-1] -= 1
                students[i] += 1
            elif  i + 1 < len(students) and students[i+1] == 2:
                students[i+1] -= 1
                students[i] += 1

    return len([i for i in students if i > 0])