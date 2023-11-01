from collections import deque

def solution(arr):
    rem = None
    answer = []
    for i in arr:
        if rem != i:
            rem = i
            answer.append(i)
    return answer