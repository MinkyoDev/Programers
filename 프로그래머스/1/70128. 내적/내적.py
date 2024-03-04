def solution(a, b):
    return sum([a[idx]*b[idx] for idx, num in enumerate(a)])