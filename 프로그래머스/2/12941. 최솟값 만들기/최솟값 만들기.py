from itertools import permutations

def solution(A,B):
    # answers = []
    # for per in list(permutations(A)):
    #     answer = sum([a * b for a, b in zip(per, B)])
    #     answers.append(answer)
    # return min(answers)
    A = sorted(A)
    B = sorted(B)[::-1]
    answer = sum([a * b for a, b in zip(A, B)])
    return answer