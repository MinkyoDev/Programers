def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        bool_list = [j=='5' or j=='0' for j in str(i)]
        if all(bool_list):
            answer.append(i)
    if not answer:
        return [-1]
    else:
        return answer