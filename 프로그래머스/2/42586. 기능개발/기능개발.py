from collections import deque
from math import ceil

def solution(progresses, speeds):
    complestion_day = deque([ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)])
    
    temp = 0
    temp_list = []
    answer = []
    for day in complestion_day:
        if day > temp:
            answer.append(len(temp_list))
            temp_list = []
            temp = day
            temp_list.append(day)
        else:
            temp_list.append(day)
    else:
        answer.append(len(temp_list))
    return answer[1:]