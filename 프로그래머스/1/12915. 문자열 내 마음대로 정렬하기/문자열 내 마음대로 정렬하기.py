def solution(strings, n):
    dict_={}
    for idx, string in enumerate(strings):
        if string[n] in dict_.keys():
            dict_[string[n]].append(string)
        else:
            dict_[string[n]]=[string]
        
    answer = sum([sorted(i) for i in [dict_[j] for j in sorted(dict_)]], [])
    return answer