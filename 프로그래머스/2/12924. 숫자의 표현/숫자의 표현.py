def solution(n):
    pibo = [sum([i for i in range(1, j+1)]) for j in range(1,145)]
    for idx, i in enumerate(pibo):
        if n <= i:
            break
    
    cnt = 0
    for j in range(1, idx+2):
        if j % 2 == 0:
            # print(0, n, j)
            if n % j == j//2:
                cnt += 1
        else:
            # print(1, n, j)
            if n % j == 0:
                cnt += 1
                
    return cnt