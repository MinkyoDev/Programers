def solution(s):
#     temp = 0
#     while s:
#         s = s.replace('()', '')
#         if temp == len(s):
#             break
#         else:
#             temp = len(s)

#     return False if s else True
    open = 0
    for i in s:
        if i == '(':
            open += 1
        elif i == ')':
            open -= 1
        
        if open < 0:
            return False
    else:
        if open == 0:
            return True
        else:
            return False