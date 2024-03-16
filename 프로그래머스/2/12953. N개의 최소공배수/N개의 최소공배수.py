def solution(arr):
    i = 1
    while True:
        temp = [(max(arr)*i)%num for num in arr]
        if sum(temp)==0:
            break
        i += 1
    return max(arr)*i