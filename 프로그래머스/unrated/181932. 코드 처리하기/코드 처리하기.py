def solution(code):
    ret = ''
    mode = 0
    for idx, i in enumerate(code):
        if i == '1' and mode == 0:
            mode = 1
        elif i == '1' and mode == 1:
            mode = 0
        else:
            if mode == 0 and idx%2 == 0:
                ret += i
            elif mode == 1 and idx%2 == 1:
                ret += i
    if ret:
        return ret
    else:
        return 'EMPTY'