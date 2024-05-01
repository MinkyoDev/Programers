def solution(s):
    num = 0
    while True:
        same = 0
        notsame = 0
        x=s[0]
        ending = False
        for i in s:
            if i == x:
                same += 1
            else:
                notsame += 1
            s = s[1:]
            if same == notsame and same != 0:
                num += 1
                if len(s) == 0:
                    ending = True
                break
        if ending:
            break
        elif len(s)==0:
            num += 1
            break
        

    return num
