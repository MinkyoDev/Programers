def solution(foods):
    num_list = [food//2 for food in foods[1:]]
    one_side = ''.join([str(idx+1) * i for idx, i in enumerate(num_list)])
    
    return one_side+'0'+one_side[::-1]