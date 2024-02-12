def solution(s):
    p_list = [i for i in s if i == 'p' or i == 'P']
    y_list = [i for i in s if i == 'y' or i == 'Y']
    return len(p_list) == len(y_list)