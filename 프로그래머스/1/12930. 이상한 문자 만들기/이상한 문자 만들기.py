def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        new_word = ''
        for idx, i in enumerate(word):
            if idx%2==0:
                new_word += i.upper()
            else:
                new_word += i.lower()
        answer.append(new_word)
    
    answer = ' '.join(answer)
    return answer