def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        divisor = [i for i in range(1, num+1) if num%i==0]
        if len(divisor) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer