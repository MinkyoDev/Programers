def solution(s):
    num = 0
    cnt = 0
    while s != '1':
        num += s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')
        cnt += 1

    return [cnt, num]