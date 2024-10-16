def solution(number, k):
    stack = []
    for i, num in enumerate(number):
        # 현재 숫자가 스택에 쌓인 마지막 숫자보다 크면 pop하고 k 줄이기
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # k가 남아있다면 뒤에서부터 k개를 자른다
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)