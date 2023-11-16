def solution(n, arr1, arr2):
    b_arry1 = [format(num, 'b').zfill(n) for num in arr1]
    b_arry2 = [format(num, 'b').zfill(n) for num in arr2]
    
    answer = []
    for num1, num2 in zip(b_arry1, b_arry2):
        string = ''
        for n1, n2 in zip(num1, num2):
            if n1 == '1' or n2 == '1':
                string += '#'
            else:
                string += ' '
        answer.append(string)
    return answer