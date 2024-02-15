def solution(n, words):
    temp = []
    for idx, word in enumerate(words):
        if word not in temp:
            if len(temp) == 0:
                temp.append(word)
            else:
                if temp[-1][-1] == word[0]:
                    temp.append(word)
                else:
                    return idx%n+1, idx//n+1
        else:
            return idx%n+1, idx//n+1
    return 0, 0