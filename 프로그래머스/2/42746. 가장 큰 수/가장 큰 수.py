def solution(numbers):
    num_strs = [str(num) for num in numbers]
    num_strs.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(num_strs)

    return answer if answer[0] != '0' else '0'