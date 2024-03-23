# def solution(n):
#     result = []
#     while True:
#         quotient, remainder = divmod(n, 3)
#         if quotient > 3:
#             result.append(remainder)
#             n = quotient
#         else:
#             result.append(remainder)
#             result.append(quotient)
#             break
#     result = int(''.join(map(str, result)))
#     result = [int(i) for i in str(result)]
#     print(result)
#     answer = sum([i*(3**idx) for idx, i in enumerate(result[::-1])])
#     return answer

def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
    return int(answer, 3)