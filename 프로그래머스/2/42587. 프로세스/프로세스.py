def solution(priorities: list, location):
    priorities = [(idx, priority) for idx, priority in enumerate(priorities)]
    answer = 0
    while priorities:
        if priorities[0][1] == max([priority[1] for priority in priorities]):
            answer += 1
            if priorities.pop(0)[0] == location:
                return answer
        else:
            priorities.append(priorities.pop(0))