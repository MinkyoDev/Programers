def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, total):
        for j in range(3, i+1):
            if i * j == total:
                if 2 * (i + j) - 4 == brown:
                    return [i, j]