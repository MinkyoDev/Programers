def solution(s, n):
    alphabets = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    
    answer = ''
    for alphabet in s:
        if alphabet == ' ':
            answer += alphabet
        else:
            alphabet_index = (alphabets.index(alphabet) + 2*n) % 52
            # if alphabet_index > len(alphabets):
            #     answer += alphabets[alphabet_index-len(alphabets)]
            # else:
            answer += alphabets[alphabet_index]

    return answer