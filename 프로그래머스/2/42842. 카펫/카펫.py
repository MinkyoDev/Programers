def solution(brown, yellow):
    for i in range(1, yellow+1):
        for j in range(1,i+1):
            if i*j == yellow:
                if (i+2)*(j+2) == (brown+yellow):
                    return [i+2, j+2]