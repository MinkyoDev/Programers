def solution(a, d, included):
    return sum([i for i,include in zip([j for j in range(a, a+d*len(included), d)],included) if include])