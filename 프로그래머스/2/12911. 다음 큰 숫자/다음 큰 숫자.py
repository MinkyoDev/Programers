def solution(n):
    cnt_one = format(n, 'b').count('1')
    
    while True:
        n += 1
        cnt = format(n, 'b').count('1')
        if cnt_one == cnt:
            break
            
    return n