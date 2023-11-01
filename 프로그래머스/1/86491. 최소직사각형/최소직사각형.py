def solution(sizes):
    return max([i[0] for i in [sorted(i) for i in sizes]]) * max([i[1] for i in [sorted(i) for i in sizes]])