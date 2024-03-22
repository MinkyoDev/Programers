def solution(s):
    answer = []
    for i in range(len(s)):
        test=[]
        for j in range(i):
            if s[i]==s[j]:
                test.append(i-j)    
        if len(test)==0:
            answer.append(-1)
        else:
            answer.append(min(test))             
    return answer